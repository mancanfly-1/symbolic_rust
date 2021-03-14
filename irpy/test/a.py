#
# WARNING: This file has been automatically generated from a.ll
#

import libirpy.itypes as itypes

def _init_types(ctx,):
  irpy = ctx['eval']
  itypes.declare_struct_type(ctx,'core::panic::Location','[0 x i64]','{ [0 x i8]*, i64 }','[0 x i32]','i32','[0 x i32]','i32','[0 x i32]',)


def _init_globals(ctx,):
  irpy = ctx['eval']
  irpy.declare_global_variable(ctx,'@AGE',itypes.parse_type(ctx,'<{ [4 x i8] }>*'),irpy.constant_struct(ctx,itypes.parse_type(ctx,'<{ [4 x i8] }>'),'<{ [4 x i8] c"\01\00\00\00" }>',),itypes.parse_type(ctx,'<{ [4 x i8] }>'))
  irpy.declare_global_constant(ctx,'@Max',itypes.parse_type(ctx,'<{ [4 x i8] }>*'),irpy.constant_struct(ctx,itypes.parse_type(ctx,'<{ [4 x i8] }>'),'<{ [4 x i8] c"\0C\00\00\00" }>',),itypes.parse_type(ctx,'<{ [4 x i8] }>'))
  irpy.declare_global_constant(ctx,'@alloc3',itypes.parse_type(ctx,'<{ [4 x i8] }>*'),irpy.constant_struct(ctx,itypes.parse_type(ctx,'<{ [4 x i8] }>'),'<{ [4 x i8] c"a_rs" }>',),itypes.parse_type(ctx,'<{ [4 x i8] }>'))
  irpy.declare_global_constant(ctx,'@alloc4',itypes.parse_type(ctx,'<{ i8*, [16 x i8] }>*'),irpy.constant_struct(ctx,itypes.parse_type(ctx,'<{ i8*, [16 x i8] }>'),'<{ i8* getelementptr inbounds (<{ [4 x i8] }>, <{ [4 x i8] }>* @alloc3, i32 0, i32 0, i32 0), [16 x i8] c"\04\00\00\00\00\00\00\00\0F\00\00\00\05\00\00\00" }>',),itypes.parse_type(ctx,'<{ i8*, [16 x i8] }>'))
  irpy.declare_global_constant(ctx,'@str_0',itypes.parse_type(ctx,'[28 x i8]*'),irpy.constant_data_array(ctx,itypes.parse_type(ctx,'[28 x i8]'),'c"attempt to add with overflow"',),itypes.parse_type(ctx,'[28 x i8]'))
  irpy.declare_global_constant(ctx,'@__rustc_debug_gdb_scripts_section__',itypes.parse_type(ctx,'[34 x i8]*'),)


def func_add(ctx,arg1,arg2,):
  irpy = ctx['eval']
  ctx['stacktrace'][-1] = {'function':'add'}
  assert itypes.has_type(ctx, arg1, itypes.parse_type(ctx,'i32')), 'Incorrect BitVec size'
  ctx.stack["%x"] = arg1
  assert itypes.has_type(ctx, arg2, itypes.parse_type(ctx,'i32')), 'Incorrect BitVec size'
  ctx.stack["%y"] = arg2
  def bb_start(pred,):
    ctx.stack["%y_dbg_spill"] = irpy.alloca(ctx,itypes.parse_type(ctx,'i32*'),irpy.constant_int(ctx,1,32,),itypes.parse_type(ctx,'i32'),)
    ctx.stack["%x_dbg_spill"] = irpy.alloca(ctx,itypes.parse_type(ctx,'i32*'),irpy.constant_int(ctx,1,32,),itypes.parse_type(ctx,'i32'),)
    irpy.store(ctx,itypes.parse_type(ctx,'void'),ctx.stack["%x"],itypes.parse_type(ctx,'i32'),ctx.stack["%x_dbg_spill"],itypes.parse_type(ctx,'i32*'),)
    irpy.store(ctx,itypes.parse_type(ctx,'void'),ctx.stack["%y"],itypes.parse_type(ctx,'i32'),ctx.stack["%y_dbg_spill"],itypes.parse_type(ctx,'i32*'),)
    irpy.debug_loc(ctx,'%0','a.rs:15:5',)
    ctx.stack["%0"] = irpy.call(ctx,itypes.parse_type(ctx,'{ i32, i1 }'),ctx.stack["%x"],itypes.parse_type(ctx,'i32'),ctx.stack["%y"],itypes.parse_type(ctx,'i32'),irpy.global_value(ctx,itypes.parse_type(ctx,'{ i32, i1 } (i32, i32)*'),'@llvm_uadd_with_overflow_i32',),itypes.parse_type(ctx,'{ i32, i1 } (i32, i32)*'),)
    irpy.debug_loc(ctx,'%_5_0','a.rs:15:5',)
    ctx.stack["%_5_0"] = irpy.extractvalue(ctx,itypes.parse_type(ctx,'i32'),ctx.stack["%0"],itypes.parse_type(ctx,'{ i32, i1 }'),)
    irpy.debug_loc(ctx,'%_5_1','a.rs:15:5',)
    ctx.stack["%_5_1"] = irpy.extractvalue(ctx,itypes.parse_type(ctx,'i1'),ctx.stack["%0"],itypes.parse_type(ctx,'{ i32, i1 }'),)
    irpy.debug_loc(ctx,'%1','a.rs:15:5',)
    ctx.stack["%1"] = irpy.call(ctx,itypes.parse_type(ctx,'i1'),ctx.stack["%_5_1"],itypes.parse_type(ctx,'i1'),irpy.constant_int(ctx,0,1,),itypes.parse_type(ctx,'i1'),irpy.global_value(ctx,itypes.parse_type(ctx,'i1 (i1, i1)*'),'@llvm_expect_i1',),itypes.parse_type(ctx,'i1 (i1, i1)*'),)
    irpy.debug_loc(ctx,'<badref>','a.rs:15:5',)
    return irpy.branch(ctx,ctx.stack["%1"],itypes.parse_type(ctx,'i1'),lambda: bb_panic("%start"),lambda: bb_bb1("%start"),)

  def bb_bb1(pred,):
    irpy.debug_loc(ctx,'<badref>','a.rs:16:2',)
    return ctx.stack["%_5_0"]

  def bb_panic(pred,):
    irpy.debug_loc(ctx,'<badref>','a.rs:15:5',)
    irpy.call(ctx,itypes.parse_type(ctx,'void'),irpy.bitcast(ctx,itypes.parse_type(ctx,'[0 x i8]*'),irpy.global_value(ctx,itypes.parse_type(ctx,'[28 x i8]*'),'@str_0',),itypes.parse_type(ctx,'[28 x i8]*'),),itypes.parse_type(ctx,'[0 x i8]*'),irpy.constant_int(ctx,28,64,),itypes.parse_type(ctx,'i64'),irpy.bitcast(ctx,itypes.parse_type(ctx,'%"core::panic::Location"*'),irpy.global_value(ctx,itypes.parse_type(ctx,'<{ i8*, [16 x i8] }>*'),'@alloc4',),itypes.parse_type(ctx,'<{ i8*, [16 x i8] }>*'),),itypes.parse_type(ctx,'%"core::panic::Location"*'),irpy.global_value(ctx,itypes.parse_type(ctx,'void ([0 x i8]*, i64, %"core::panic::Location"*)*'),'@_ZN4core9panicking5panic17h68e56c2eeba99c8cE',),itypes.parse_type(ctx,'void ([0 x i8]*, i64, %"core::panic::Location"*)*'),)
    irpy.debug_loc(ctx,'<badref>','a.rs:15:5',)
    irpy.unreachable(ctx,itypes.parse_type(ctx,'void'),)

  return bb_start(None)

def _init_metadata(ctx,):
  irpy = ctx['eval']
  irpy.declare_metadata(ctx, '!0','!DIGlobalVariableExpression(var: !1, expr: !DIExpression())')
  irpy.declare_metadata(ctx, '!1','distinct !DIGlobalVariable(name: "AGE", scope: !2, file: !3, line: 3, type: !4, isLocal: false, isDefinition: true, align: 4)')
  irpy.declare_metadata(ctx, '!2','!DINamespace(name: "a", scope: null)')
  irpy.declare_metadata(ctx, '!3','!DIFile(filename: "a.rs", directory: "/home/mancanfly/Downloads/hv6/test_rust/test1/src", checksumkind: CSK_MD5, checksum: "e216e937b8d6cec3bd7e7ee77b8278e6")')
  irpy.declare_metadata(ctx, '!4','!DIBasicType(name: "u32", size: 32, encoding: DW_ATE_unsigned)')
  irpy.declare_metadata(ctx, '!5','!DIGlobalVariableExpression(var: !6, expr: !DIExpression())')
  irpy.declare_metadata(ctx, '!6','distinct !DIGlobalVariable(name: "Max", scope: !2, file: !3, line: 5, type: !4, isLocal: false, isDefinition: true, align: 4)')
  irpy.declare_metadata(ctx, '!10','distinct !DICompileUnit(language: DW_LANG_Rust, file: !11, producer: "clang LLVM (rustc version 1.46.0-nightly (7750c3d46 2020-06-26))", isOptimized: false, runtimeVersion: 0, emissionKind: FullDebug, enums: !12, globals: !13)')
  irpy.declare_metadata(ctx, '!11','!DIFile(filename: "a.rs", directory: "/home/mancanfly/Downloads/hv6/test_rust/test1/src")')
  irpy.declare_metadata(ctx, '!12','!{}')
  irpy.declare_metadata(ctx, '!13','!{!0, !5}')
  irpy.declare_metadata(ctx, '!14','distinct !DISubprogram(name: "add", scope: !2, file: !3, line: 7, type: !15, scopeLine: 7, flags: DIFlagPrototyped, spFlags: DISPFlagDefinition, unit: !10, templateParams: !12, retainedNodes: !17)')
  irpy.declare_metadata(ctx, '!15','!DISubroutineType(types: !16)')
  irpy.declare_metadata(ctx, '!16','!{!4, !4, !4}')
  irpy.declare_metadata(ctx, '!17','!{!18, !19}')
  irpy.declare_metadata(ctx, '!18','!DILocalVariable(name: "x", arg: 1, scope: !14, file: !3, line: 7, type: !4)')
  irpy.declare_metadata(ctx, '!19','!DILocalVariable(name: "y", arg: 2, scope: !14, file: !3, line: 7, type: !4)')
  irpy.declare_metadata(ctx, '!20','!DILocation(line: 7, column: 19, scope: !14)')
  irpy.declare_metadata(ctx, '!21','!DILocation(line: 7, column: 26, scope: !14)')
  irpy.declare_metadata(ctx, '!22','!DILocation(line: 15, column: 5, scope: !14)')
  irpy.declare_metadata(ctx, '!23','!DILocation(line: 16, column: 2, scope: !14)')

