import streamlit as st
import llvmlite.ir as ir
import llvmlite.binding as llvm

# Streamlit app title
st.title("LLVM JIT Compilation with llvmlite")

# Define an LLVM module and function
module = ir.Module(name="example")
func_type = ir.FunctionType(ir.IntType(32), [])
function = ir.Function(module, func_type, name="main")

# Create a basic block
block = function.append_basic_block(name="entry")
builder = ir.IRBuilder(block)

# Add instructions
int_const = ir.Constant(ir.IntType(32), 42)
builder.ret(int_const)

# Display the generated IR
st.subheader("Generated LLVM IR:")
st.code(str(module), language="llvm")

# Initialize LLVM and JIT the module
llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()

# Compile the module
target = llvm.Target.from_default_triple()
target_machine = target.create_target_machine()
compiled_module = llvm.parse_assembly(str(module))
compiled_module.verify()
execution_engine = llvm.create_mcjit_compiler(compiled_module, target_machine)

# Execute the function
execution_engine.finalize_object()
entry = execution_engine.get_function_address("main")

# Convert entry (function pointer) to a Python-callable function
import ctypes

cfunc = ctypes.CFUNCTYPE(ctypes.c_int32)(entry)
result = cfunc()

# Display the result in the browser
st.subheader("Execution Result:")
st.write(f"The function returned: {result}")
