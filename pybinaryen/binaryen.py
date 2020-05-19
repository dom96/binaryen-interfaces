"""
Python interface to the binaryen webassembly library (https://github.com/WebAssembly/binaryen)

Author: Irmen de Jong (irmen@razorvine.net)
Software license: "MIT software license". See http://opensource.org/licenses/MIT
"""

__version__ = "1.3"

from _binaryen import ffi, lib


def import_functions():
    # generate function names in this module are without the 'Binaryen' prefix.
    import inspect
    _current_module = __import__(__name__)
    for name, member in inspect.getmembers(lib):
        pname = name
        if inspect.isroutine(member):
            if name.startswith("Binaryen"):
                pname = name[8:]
        setattr(_current_module, pname, member)
        print("{} = lib.{}".format(pname, name))

# import_functions()
del import_functions

# The following list of functions was generated by the code above,
# but included here statically for IDE/code completion purposes (and to remove the Binaryen prefix)
AbsFloat32 = lib.BinaryenAbsFloat32
AbsFloat64 = lib.BinaryenAbsFloat64
AbsVecF32x4 = lib.BinaryenAbsVecF32x4
AbsVecF64x2 = lib.BinaryenAbsVecF64x2
AbsVecI16x8 = lib.BinaryenAbsVecI16x8
AbsVecI32x4 = lib.BinaryenAbsVecI32x4
AbsVecI8x16 = lib.BinaryenAbsVecI8x16
AddCustomSection = lib.BinaryenAddCustomSection
AddEvent = lib.BinaryenAddEvent
AddEventExport = lib.BinaryenAddEventExport
AddEventImport = lib.BinaryenAddEventImport
AddFloat32 = lib.BinaryenAddFloat32
AddFloat64 = lib.BinaryenAddFloat64
AddFunction = lib.BinaryenAddFunction
AddFunctionExport = lib.BinaryenAddFunctionExport
AddFunctionImport = lib.BinaryenAddFunctionImport
AddGlobal = lib.BinaryenAddGlobal
AddGlobalExport = lib.BinaryenAddGlobalExport
AddGlobalImport = lib.BinaryenAddGlobalImport
AddInt32 = lib.BinaryenAddInt32
AddInt64 = lib.BinaryenAddInt64
AddMemoryExport = lib.BinaryenAddMemoryExport
AddMemoryImport = lib.BinaryenAddMemoryImport
AddSatSVecI16x8 = lib.BinaryenAddSatSVecI16x8
AddSatSVecI8x16 = lib.BinaryenAddSatSVecI8x16
AddSatUVecI16x8 = lib.BinaryenAddSatUVecI16x8
AddSatUVecI8x16 = lib.BinaryenAddSatUVecI8x16
AddTableExport = lib.BinaryenAddTableExport
AddTableImport = lib.BinaryenAddTableImport
AddVecF32x4 = lib.BinaryenAddVecF32x4
AddVecF64x2 = lib.BinaryenAddVecF64x2
AddVecI16x8 = lib.BinaryenAddVecI16x8
AddVecI32x4 = lib.BinaryenAddVecI32x4
AddVecI64x2 = lib.BinaryenAddVecI64x2
AddVecI8x16 = lib.BinaryenAddVecI8x16
AllTrueVecI16x8 = lib.BinaryenAllTrueVecI16x8
AllTrueVecI32x4 = lib.BinaryenAllTrueVecI32x4
AllTrueVecI64x2 = lib.BinaryenAllTrueVecI64x2
AllTrueVecI8x16 = lib.BinaryenAllTrueVecI8x16
AndInt32 = lib.BinaryenAndInt32
AndInt64 = lib.BinaryenAndInt64
AndNotVec128 = lib.BinaryenAndNotVec128
AndVec128 = lib.BinaryenAndVec128
AnyTrueVecI16x8 = lib.BinaryenAnyTrueVecI16x8
AnyTrueVecI32x4 = lib.BinaryenAnyTrueVecI32x4
AnyTrueVecI64x2 = lib.BinaryenAnyTrueVecI64x2
AnyTrueVecI8x16 = lib.BinaryenAnyTrueVecI8x16
AreColorsEnabled = lib.BinaryenAreColorsEnabled
AtomicCmpxchg = lib.BinaryenAtomicCmpxchg
AtomicCmpxchgGetBytes = lib.BinaryenAtomicCmpxchgGetBytes
AtomicCmpxchgGetExpected = lib.BinaryenAtomicCmpxchgGetExpected
AtomicCmpxchgGetOffset = lib.BinaryenAtomicCmpxchgGetOffset
AtomicCmpxchgGetPtr = lib.BinaryenAtomicCmpxchgGetPtr
AtomicCmpxchgGetReplacement = lib.BinaryenAtomicCmpxchgGetReplacement
AtomicCmpxchgId = lib.BinaryenAtomicCmpxchgId
AtomicFence = lib.BinaryenAtomicFence
AtomicFenceGetOrder = lib.BinaryenAtomicFenceGetOrder
AtomicFenceId = lib.BinaryenAtomicFenceId
AtomicLoad = lib.BinaryenAtomicLoad
AtomicNotify = lib.BinaryenAtomicNotify
AtomicNotifyGetNotifyCount = lib.BinaryenAtomicNotifyGetNotifyCount
AtomicNotifyGetPtr = lib.BinaryenAtomicNotifyGetPtr
AtomicNotifyId = lib.BinaryenAtomicNotifyId
AtomicRMW = lib.BinaryenAtomicRMW
AtomicRMWAdd = lib.BinaryenAtomicRMWAdd
AtomicRMWAnd = lib.BinaryenAtomicRMWAnd
AtomicRMWGetBytes = lib.BinaryenAtomicRMWGetBytes
AtomicRMWGetOffset = lib.BinaryenAtomicRMWGetOffset
AtomicRMWGetOp = lib.BinaryenAtomicRMWGetOp
AtomicRMWGetPtr = lib.BinaryenAtomicRMWGetPtr
AtomicRMWGetValue = lib.BinaryenAtomicRMWGetValue
AtomicRMWId = lib.BinaryenAtomicRMWId
AtomicRMWOr = lib.BinaryenAtomicRMWOr
AtomicRMWSub = lib.BinaryenAtomicRMWSub
AtomicRMWXchg = lib.BinaryenAtomicRMWXchg
AtomicRMWXor = lib.BinaryenAtomicRMWXor
AtomicStore = lib.BinaryenAtomicStore
AtomicWait = lib.BinaryenAtomicWait
AtomicWaitGetExpected = lib.BinaryenAtomicWaitGetExpected
AtomicWaitGetExpectedType = lib.BinaryenAtomicWaitGetExpectedType
AtomicWaitGetPtr = lib.BinaryenAtomicWaitGetPtr
AtomicWaitGetTimeout = lib.BinaryenAtomicWaitGetTimeout
AtomicWaitId = lib.BinaryenAtomicWaitId
AvgrUVecI16x8 = lib.BinaryenAvgrUVecI16x8
AvgrUVecI8x16 = lib.BinaryenAvgrUVecI8x16
Binary = lib.BinaryenBinary
BinaryGetLeft = lib.BinaryenBinaryGetLeft
BinaryGetOp = lib.BinaryenBinaryGetOp
BinaryGetRight = lib.BinaryenBinaryGetRight
BinaryId = lib.BinaryenBinaryId
BitmaskVecI16x8 = lib.BinaryenBitmaskVecI16x8
BitmaskVecI32x4 = lib.BinaryenBitmaskVecI32x4
BitmaskVecI8x16 = lib.BinaryenBitmaskVecI8x16
BitselectVec128 = lib.BinaryenBitselectVec128
Block = lib.BinaryenBlock
BlockGetChild = lib.BinaryenBlockGetChild
BlockGetName = lib.BinaryenBlockGetName
BlockGetNumChildren = lib.BinaryenBlockGetNumChildren
BlockId = lib.BinaryenBlockId
BrOnExn = lib.BinaryenBrOnExn
BrOnExnGetEvent = lib.BinaryenBrOnExnGetEvent
BrOnExnGetExnref = lib.BinaryenBrOnExnGetExnref
BrOnExnGetName = lib.BinaryenBrOnExnGetName
BrOnExnId = lib.BinaryenBrOnExnId
Break = lib.BinaryenBreak
BreakGetCondition = lib.BinaryenBreakGetCondition
BreakGetName = lib.BinaryenBreakGetName
BreakGetValue = lib.BinaryenBreakGetValue
BreakId = lib.BinaryenBreakId
Call = lib.BinaryenCall
CallGetNumOperands = lib.BinaryenCallGetNumOperands
CallGetOperand = lib.BinaryenCallGetOperand
CallGetTarget = lib.BinaryenCallGetTarget
CallId = lib.BinaryenCallId
CallIndirect = lib.BinaryenCallIndirect
CallIndirectGetNumOperands = lib.BinaryenCallIndirectGetNumOperands
CallIndirectGetOperand = lib.BinaryenCallIndirectGetOperand
CallIndirectGetTarget = lib.BinaryenCallIndirectGetTarget
CallIndirectId = lib.BinaryenCallIndirectId
CallIndirectIsReturn = lib.BinaryenCallIndirectIsReturn
CallIsReturn = lib.BinaryenCallIsReturn
CeilFloat32 = lib.BinaryenCeilFloat32
CeilFloat64 = lib.BinaryenCeilFloat64
ClearPassArguments = lib.BinaryenClearPassArguments
ClzInt32 = lib.BinaryenClzInt32
ClzInt64 = lib.BinaryenClzInt64
Const = lib.BinaryenConst
ConstGetValueF32 = lib.BinaryenConstGetValueF32
ConstGetValueF64 = lib.BinaryenConstGetValueF64
ConstGetValueI32 = lib.BinaryenConstGetValueI32
ConstGetValueI64 = lib.BinaryenConstGetValueI64
ConstGetValueI64High = lib.BinaryenConstGetValueI64High
ConstGetValueI64Low = lib.BinaryenConstGetValueI64Low
ConstGetValueV128 = lib.BinaryenConstGetValueV128
ConstId = lib.BinaryenConstId
ConvertSInt32ToFloat32 = lib.BinaryenConvertSInt32ToFloat32
ConvertSInt32ToFloat64 = lib.BinaryenConvertSInt32ToFloat64
ConvertSInt64ToFloat32 = lib.BinaryenConvertSInt64ToFloat32
ConvertSInt64ToFloat64 = lib.BinaryenConvertSInt64ToFloat64
ConvertSVecI32x4ToVecF32x4 = lib.BinaryenConvertSVecI32x4ToVecF32x4
ConvertSVecI64x2ToVecF64x2 = lib.BinaryenConvertSVecI64x2ToVecF64x2
ConvertUInt32ToFloat32 = lib.BinaryenConvertUInt32ToFloat32
ConvertUInt32ToFloat64 = lib.BinaryenConvertUInt32ToFloat64
ConvertUInt64ToFloat32 = lib.BinaryenConvertUInt64ToFloat32
ConvertUInt64ToFloat64 = lib.BinaryenConvertUInt64ToFloat64
ConvertUVecI32x4ToVecF32x4 = lib.BinaryenConvertUVecI32x4ToVecF32x4
ConvertUVecI64x2ToVecF64x2 = lib.BinaryenConvertUVecI64x2ToVecF64x2
CopyMemorySegmentData = lib.BinaryenCopyMemorySegmentData
CopySignFloat32 = lib.BinaryenCopySignFloat32
CopySignFloat64 = lib.BinaryenCopySignFloat64
CtzInt32 = lib.BinaryenCtzInt32
CtzInt64 = lib.BinaryenCtzInt64
DataDrop = lib.BinaryenDataDrop
DataDropGetSegment = lib.BinaryenDataDropGetSegment
DataDropId = lib.BinaryenDataDropId
DemoteFloat64 = lib.BinaryenDemoteFloat64
DivFloat32 = lib.BinaryenDivFloat32
DivFloat64 = lib.BinaryenDivFloat64
DivSInt32 = lib.BinaryenDivSInt32
DivSInt64 = lib.BinaryenDivSInt64
DivUInt32 = lib.BinaryenDivUInt32
DivUInt64 = lib.BinaryenDivUInt64
DivVecF32x4 = lib.BinaryenDivVecF32x4
DivVecF64x2 = lib.BinaryenDivVecF64x2
DotSVecI16x8ToVecI32x4 = lib.BinaryenDotSVecI16x8ToVecI32x4
Drop = lib.BinaryenDrop
DropGetValue = lib.BinaryenDropGetValue
DropId = lib.BinaryenDropId
EqFloat32 = lib.BinaryenEqFloat32
EqFloat64 = lib.BinaryenEqFloat64
EqInt32 = lib.BinaryenEqInt32
EqInt64 = lib.BinaryenEqInt64
EqVecF32x4 = lib.BinaryenEqVecF32x4
EqVecF64x2 = lib.BinaryenEqVecF64x2
EqVecI16x8 = lib.BinaryenEqVecI16x8
EqVecI32x4 = lib.BinaryenEqVecI32x4
EqVecI8x16 = lib.BinaryenEqVecI8x16
EqZInt32 = lib.BinaryenEqZInt32
EqZInt64 = lib.BinaryenEqZInt64
EventGetAttribute = lib.BinaryenEventGetAttribute
EventGetName = lib.BinaryenEventGetName
EventGetParams = lib.BinaryenEventGetParams
EventGetResults = lib.BinaryenEventGetResults
EventImportGetBase = lib.BinaryenEventImportGetBase
EventImportGetModule = lib.BinaryenEventImportGetModule
ExportGetKind = lib.BinaryenExportGetKind
ExportGetName = lib.BinaryenExportGetName
ExportGetValue = lib.BinaryenExportGetValue
ExpressionCopy = lib.BinaryenExpressionCopy
ExpressionGetId = lib.BinaryenExpressionGetId
ExpressionGetSideEffects = lib.BinaryenExpressionGetSideEffects
ExpressionGetType = lib.BinaryenExpressionGetType
ExpressionPrint = lib.BinaryenExpressionPrint
ExtendS16Int32 = lib.BinaryenExtendS16Int32
ExtendS16Int64 = lib.BinaryenExtendS16Int64
ExtendS32Int64 = lib.BinaryenExtendS32Int64
ExtendS8Int32 = lib.BinaryenExtendS8Int32
ExtendS8Int64 = lib.BinaryenExtendS8Int64
ExtendSInt32 = lib.BinaryenExtendSInt32
ExtendUInt32 = lib.BinaryenExtendUInt32
ExternalEvent = lib.BinaryenExternalEvent
ExternalFunction = lib.BinaryenExternalFunction
ExternalGlobal = lib.BinaryenExternalGlobal
ExternalMemory = lib.BinaryenExternalMemory
ExternalTable = lib.BinaryenExternalTable
ExtractLaneSVecI16x8 = lib.BinaryenExtractLaneSVecI16x8
ExtractLaneSVecI8x16 = lib.BinaryenExtractLaneSVecI8x16
ExtractLaneUVecI16x8 = lib.BinaryenExtractLaneUVecI16x8
ExtractLaneUVecI8x16 = lib.BinaryenExtractLaneUVecI8x16
ExtractLaneVecF32x4 = lib.BinaryenExtractLaneVecF32x4
ExtractLaneVecF64x2 = lib.BinaryenExtractLaneVecF64x2
ExtractLaneVecI32x4 = lib.BinaryenExtractLaneVecI32x4
ExtractLaneVecI64x2 = lib.BinaryenExtractLaneVecI64x2
FeatureAll = lib.BinaryenFeatureAll
FeatureAtomics = lib.BinaryenFeatureAtomics
FeatureBulkMemory = lib.BinaryenFeatureBulkMemory
FeatureExceptionHandling = lib.BinaryenFeatureExceptionHandling
FeatureMVP = lib.BinaryenFeatureMVP
FeatureMultivalue = lib.BinaryenFeatureMultivalue
FeatureMutableGlobals = lib.BinaryenFeatureMutableGlobals
FeatureNontrappingFPToInt = lib.BinaryenFeatureNontrappingFPToInt
FeatureReferenceTypes = lib.BinaryenFeatureReferenceTypes
FeatureSIMD128 = lib.BinaryenFeatureSIMD128
FeatureSignExt = lib.BinaryenFeatureSignExt
FeatureTailCall = lib.BinaryenFeatureTailCall
FloorFloat32 = lib.BinaryenFloorFloat32
FloorFloat64 = lib.BinaryenFloorFloat64
FunctionGetBody = lib.BinaryenFunctionGetBody
FunctionGetName = lib.BinaryenFunctionGetName
FunctionGetNumVars = lib.BinaryenFunctionGetNumVars
FunctionGetParams = lib.BinaryenFunctionGetParams
FunctionGetResults = lib.BinaryenFunctionGetResults
FunctionGetVar = lib.BinaryenFunctionGetVar
FunctionImportGetBase = lib.BinaryenFunctionImportGetBase
FunctionImportGetModule = lib.BinaryenFunctionImportGetModule
FunctionOptimize = lib.BinaryenFunctionOptimize
FunctionRunPasses = lib.BinaryenFunctionRunPasses
FunctionSetDebugLocation = lib.BinaryenFunctionSetDebugLocation
GeFloat32 = lib.BinaryenGeFloat32
GeFloat64 = lib.BinaryenGeFloat64
GeSInt32 = lib.BinaryenGeSInt32
GeSInt64 = lib.BinaryenGeSInt64
GeSVecI16x8 = lib.BinaryenGeSVecI16x8
GeSVecI32x4 = lib.BinaryenGeSVecI32x4
GeSVecI8x16 = lib.BinaryenGeSVecI8x16
GeUInt32 = lib.BinaryenGeUInt32
GeUInt64 = lib.BinaryenGeUInt64
GeUVecI16x8 = lib.BinaryenGeUVecI16x8
GeUVecI32x4 = lib.BinaryenGeUVecI32x4
GeUVecI8x16 = lib.BinaryenGeUVecI8x16
GeVecF32x4 = lib.BinaryenGeVecF32x4
GeVecF64x2 = lib.BinaryenGeVecF64x2
GetAlwaysInlineMaxSize = lib.BinaryenGetAlwaysInlineMaxSize
GetDebugInfo = lib.BinaryenGetDebugInfo
GetEvent = lib.BinaryenGetEvent
GetExportByIndex = lib.BinaryenGetExportByIndex
GetFlexibleInlineMaxSize = lib.BinaryenGetFlexibleInlineMaxSize
GetFunction = lib.BinaryenGetFunction
GetFunctionByIndex = lib.BinaryenGetFunctionByIndex
GetFunctionTableSegmentData = lib.BinaryenGetFunctionTableSegmentData
GetFunctionTableSegmentLength = lib.BinaryenGetFunctionTableSegmentLength
GetFunctionTableSegmentOffset = lib.BinaryenGetFunctionTableSegmentOffset
GetGlobal = lib.BinaryenGetGlobal
GetLowMemoryUnused = lib.BinaryenGetLowMemoryUnused
GetMemorySegmentByteLength = lib.BinaryenGetMemorySegmentByteLength
GetMemorySegmentByteOffset = lib.BinaryenGetMemorySegmentByteOffset
GetMemorySegmentPassive = lib.BinaryenGetMemorySegmentPassive
GetNumExports = lib.BinaryenGetNumExports
GetNumFunctionTableSegments = lib.BinaryenGetNumFunctionTableSegments
GetNumFunctions = lib.BinaryenGetNumFunctions
GetNumMemorySegments = lib.BinaryenGetNumMemorySegments
GetOneCallerInlineMaxSize = lib.BinaryenGetOneCallerInlineMaxSize
GetOptimizeLevel = lib.BinaryenGetOptimizeLevel
GetPassArgument = lib.BinaryenGetPassArgument
GetShrinkLevel = lib.BinaryenGetShrinkLevel
GlobalGet = lib.BinaryenGlobalGet
GlobalGetGetName = lib.BinaryenGlobalGetGetName
GlobalGetId = lib.BinaryenGlobalGetId
GlobalGetInitExpr = lib.BinaryenGlobalGetInitExpr
GlobalGetName = lib.BinaryenGlobalGetName
GlobalGetType = lib.BinaryenGlobalGetType
GlobalImportGetBase = lib.BinaryenGlobalImportGetBase
GlobalImportGetModule = lib.BinaryenGlobalImportGetModule
GlobalIsMutable = lib.BinaryenGlobalIsMutable
GlobalSet = lib.BinaryenGlobalSet
GlobalSetGetName = lib.BinaryenGlobalSetGetName
GlobalSetGetValue = lib.BinaryenGlobalSetGetValue
GlobalSetId = lib.BinaryenGlobalSetId
GtFloat32 = lib.BinaryenGtFloat32
GtFloat64 = lib.BinaryenGtFloat64
GtSInt32 = lib.BinaryenGtSInt32
GtSInt64 = lib.BinaryenGtSInt64
GtSVecI16x8 = lib.BinaryenGtSVecI16x8
GtSVecI32x4 = lib.BinaryenGtSVecI32x4
GtSVecI8x16 = lib.BinaryenGtSVecI8x16
GtUInt32 = lib.BinaryenGtUInt32
GtUInt64 = lib.BinaryenGtUInt64
GtUVecI16x8 = lib.BinaryenGtUVecI16x8
GtUVecI32x4 = lib.BinaryenGtUVecI32x4
GtUVecI8x16 = lib.BinaryenGtUVecI8x16
GtVecF32x4 = lib.BinaryenGtVecF32x4
GtVecF64x2 = lib.BinaryenGtVecF64x2
Host = lib.BinaryenHost
HostGetNameOperand = lib.BinaryenHostGetNameOperand
HostGetNumOperands = lib.BinaryenHostGetNumOperands
HostGetOp = lib.BinaryenHostGetOp
HostGetOperand = lib.BinaryenHostGetOperand
HostId = lib.BinaryenHostId
If = lib.BinaryenIf
IfGetCondition = lib.BinaryenIfGetCondition
IfGetIfFalse = lib.BinaryenIfGetIfFalse
IfGetIfTrue = lib.BinaryenIfGetIfTrue
IfId = lib.BinaryenIfId
InvalidId = lib.BinaryenInvalidId
IsFunctionTableImported = lib.BinaryenIsFunctionTableImported
LeFloat32 = lib.BinaryenLeFloat32
LeFloat64 = lib.BinaryenLeFloat64
LeSInt32 = lib.BinaryenLeSInt32
LeSInt64 = lib.BinaryenLeSInt64
LeSVecI16x8 = lib.BinaryenLeSVecI16x8
LeSVecI32x4 = lib.BinaryenLeSVecI32x4
LeSVecI8x16 = lib.BinaryenLeSVecI8x16
LeUInt32 = lib.BinaryenLeUInt32
LeUInt64 = lib.BinaryenLeUInt64
LeUVecI16x8 = lib.BinaryenLeUVecI16x8
LeUVecI32x4 = lib.BinaryenLeUVecI32x4
LeUVecI8x16 = lib.BinaryenLeUVecI8x16
LeVecF32x4 = lib.BinaryenLeVecF32x4
LeVecF64x2 = lib.BinaryenLeVecF64x2
LiteralFloat32 = lib.BinaryenLiteralFloat32
LiteralFloat32Bits = lib.BinaryenLiteralFloat32Bits
LiteralFloat64 = lib.BinaryenLiteralFloat64
LiteralFloat64Bits = lib.BinaryenLiteralFloat64Bits
LiteralInt32 = lib.BinaryenLiteralInt32
LiteralInt64 = lib.BinaryenLiteralInt64
LiteralVec128 = lib.BinaryenLiteralVec128
Load = lib.BinaryenLoad
LoadExtSVec16x4ToVecI32x4 = lib.BinaryenLoadExtSVec16x4ToVecI32x4
LoadExtSVec32x2ToVecI64x2 = lib.BinaryenLoadExtSVec32x2ToVecI64x2
LoadExtSVec8x8ToVecI16x8 = lib.BinaryenLoadExtSVec8x8ToVecI16x8
LoadExtUVec16x4ToVecI32x4 = lib.BinaryenLoadExtUVec16x4ToVecI32x4
LoadExtUVec32x2ToVecI64x2 = lib.BinaryenLoadExtUVec32x2ToVecI64x2
LoadExtUVec8x8ToVecI16x8 = lib.BinaryenLoadExtUVec8x8ToVecI16x8
LoadGetAlign = lib.BinaryenLoadGetAlign
LoadGetBytes = lib.BinaryenLoadGetBytes
LoadGetOffset = lib.BinaryenLoadGetOffset
LoadGetPtr = lib.BinaryenLoadGetPtr
LoadId = lib.BinaryenLoadId
LoadIsAtomic = lib.BinaryenLoadIsAtomic
LoadIsSigned = lib.BinaryenLoadIsSigned
LoadSplatVec16x8 = lib.BinaryenLoadSplatVec16x8
LoadSplatVec32x4 = lib.BinaryenLoadSplatVec32x4
LoadSplatVec64x2 = lib.BinaryenLoadSplatVec64x2
LoadSplatVec8x16 = lib.BinaryenLoadSplatVec8x16
LocalGet = lib.BinaryenLocalGet
LocalGetGetIndex = lib.BinaryenLocalGetGetIndex
LocalGetId = lib.BinaryenLocalGetId
LocalSet = lib.BinaryenLocalSet
LocalSetGetIndex = lib.BinaryenLocalSetGetIndex
LocalSetGetValue = lib.BinaryenLocalSetGetValue
LocalSetId = lib.BinaryenLocalSetId
LocalSetIsTee = lib.BinaryenLocalSetIsTee
LocalTee = lib.BinaryenLocalTee
Loop = lib.BinaryenLoop
LoopGetBody = lib.BinaryenLoopGetBody
LoopGetName = lib.BinaryenLoopGetName
LoopId = lib.BinaryenLoopId
LtFloat32 = lib.BinaryenLtFloat32
LtFloat64 = lib.BinaryenLtFloat64
LtSInt32 = lib.BinaryenLtSInt32
LtSInt64 = lib.BinaryenLtSInt64
LtSVecI16x8 = lib.BinaryenLtSVecI16x8
LtSVecI32x4 = lib.BinaryenLtSVecI32x4
LtSVecI8x16 = lib.BinaryenLtSVecI8x16
LtUInt32 = lib.BinaryenLtUInt32
LtUInt64 = lib.BinaryenLtUInt64
LtUVecI16x8 = lib.BinaryenLtUVecI16x8
LtUVecI32x4 = lib.BinaryenLtUVecI32x4
LtUVecI8x16 = lib.BinaryenLtUVecI8x16
LtVecF32x4 = lib.BinaryenLtVecF32x4
LtVecF64x2 = lib.BinaryenLtVecF64x2
MaxFloat32 = lib.BinaryenMaxFloat32
MaxFloat64 = lib.BinaryenMaxFloat64
MaxSVecI16x8 = lib.BinaryenMaxSVecI16x8
MaxSVecI32x4 = lib.BinaryenMaxSVecI32x4
MaxSVecI8x16 = lib.BinaryenMaxSVecI8x16
MaxUVecI16x8 = lib.BinaryenMaxUVecI16x8
MaxUVecI32x4 = lib.BinaryenMaxUVecI32x4
MaxUVecI8x16 = lib.BinaryenMaxUVecI8x16
MaxVecF32x4 = lib.BinaryenMaxVecF32x4
MaxVecF64x2 = lib.BinaryenMaxVecF64x2
MemoryCopy = lib.BinaryenMemoryCopy
MemoryCopyGetDest = lib.BinaryenMemoryCopyGetDest
MemoryCopyGetSize = lib.BinaryenMemoryCopyGetSize
MemoryCopyGetSource = lib.BinaryenMemoryCopyGetSource
MemoryCopyId = lib.BinaryenMemoryCopyId
MemoryFill = lib.BinaryenMemoryFill
MemoryFillGetDest = lib.BinaryenMemoryFillGetDest
MemoryFillGetSize = lib.BinaryenMemoryFillGetSize
MemoryFillGetValue = lib.BinaryenMemoryFillGetValue
MemoryFillId = lib.BinaryenMemoryFillId
MemoryGrow = lib.BinaryenMemoryGrow
MemoryInit = lib.BinaryenMemoryInit
MemoryInitGetDest = lib.BinaryenMemoryInitGetDest
MemoryInitGetOffset = lib.BinaryenMemoryInitGetOffset
MemoryInitGetSegment = lib.BinaryenMemoryInitGetSegment
MemoryInitGetSize = lib.BinaryenMemoryInitGetSize
MemoryInitId = lib.BinaryenMemoryInitId
MemorySize = lib.BinaryenMemorySize
MinFloat32 = lib.BinaryenMinFloat32
MinFloat64 = lib.BinaryenMinFloat64
MinSVecI16x8 = lib.BinaryenMinSVecI16x8
MinSVecI32x4 = lib.BinaryenMinSVecI32x4
MinSVecI8x16 = lib.BinaryenMinSVecI8x16
MinUVecI16x8 = lib.BinaryenMinUVecI16x8
MinUVecI32x4 = lib.BinaryenMinUVecI32x4
MinUVecI8x16 = lib.BinaryenMinUVecI8x16
MinVecF32x4 = lib.BinaryenMinVecF32x4
MinVecF64x2 = lib.BinaryenMinVecF64x2
ModuleAddDebugInfoFileName = lib.BinaryenModuleAddDebugInfoFileName
ModuleAllocateAndWrite = lib.BinaryenModuleAllocateAndWrite
ModuleAllocateAndWriteText = lib.BinaryenModuleAllocateAndWriteText
ModuleAutoDrop = lib.BinaryenModuleAutoDrop
ModuleCreate = lib.BinaryenModuleCreate
ModuleDispose = lib.BinaryenModuleDispose
ModuleGetDebugInfoFileName = lib.BinaryenModuleGetDebugInfoFileName
ModuleGetFeatures = lib.BinaryenModuleGetFeatures
ModuleInterpret = lib.BinaryenModuleInterpret
ModuleOptimize = lib.BinaryenModuleOptimize
ModuleParse = lib.BinaryenModuleParse
ModulePrint = lib.BinaryenModulePrint
ModulePrintAsmjs = lib.BinaryenModulePrintAsmjs
ModuleRead = lib.BinaryenModuleRead
ModuleRunPasses = lib.BinaryenModuleRunPasses
ModuleSetFeatures = lib.BinaryenModuleSetFeatures
ModuleValidate = lib.BinaryenModuleValidate
ModuleWrite = lib.BinaryenModuleWrite
ModuleWriteText = lib.BinaryenModuleWriteText
ModuleWriteWithSourceMap = lib.BinaryenModuleWriteWithSourceMap
MulFloat32 = lib.BinaryenMulFloat32
MulFloat64 = lib.BinaryenMulFloat64
MulInt32 = lib.BinaryenMulInt32
MulInt64 = lib.BinaryenMulInt64
MulVecF32x4 = lib.BinaryenMulVecF32x4
MulVecF64x2 = lib.BinaryenMulVecF64x2
MulVecI16x8 = lib.BinaryenMulVecI16x8
MulVecI32x4 = lib.BinaryenMulVecI32x4
MulVecI64x2 = lib.BinaryenMulVecI64x2
MulVecI8x16 = lib.BinaryenMulVecI8x16
NarrowSVecI16x8ToVecI8x16 = lib.BinaryenNarrowSVecI16x8ToVecI8x16
NarrowSVecI32x4ToVecI16x8 = lib.BinaryenNarrowSVecI32x4ToVecI16x8
NarrowUVecI16x8ToVecI8x16 = lib.BinaryenNarrowUVecI16x8ToVecI8x16
NarrowUVecI32x4ToVecI16x8 = lib.BinaryenNarrowUVecI32x4ToVecI16x8
NeFloat32 = lib.BinaryenNeFloat32
NeFloat64 = lib.BinaryenNeFloat64
NeInt32 = lib.BinaryenNeInt32
NeInt64 = lib.BinaryenNeInt64
NeVecF32x4 = lib.BinaryenNeVecF32x4
NeVecF64x2 = lib.BinaryenNeVecF64x2
NeVecI16x8 = lib.BinaryenNeVecI16x8
NeVecI32x4 = lib.BinaryenNeVecI32x4
NeVecI8x16 = lib.BinaryenNeVecI8x16
NearestFloat32 = lib.BinaryenNearestFloat32
NearestFloat64 = lib.BinaryenNearestFloat64
NegFloat32 = lib.BinaryenNegFloat32
NegFloat64 = lib.BinaryenNegFloat64
NegVecF32x4 = lib.BinaryenNegVecF32x4
NegVecF64x2 = lib.BinaryenNegVecF64x2
NegVecI16x8 = lib.BinaryenNegVecI16x8
NegVecI32x4 = lib.BinaryenNegVecI32x4
NegVecI64x2 = lib.BinaryenNegVecI64x2
NegVecI8x16 = lib.BinaryenNegVecI8x16
Nop = lib.BinaryenNop
NopId = lib.BinaryenNopId
NotVec128 = lib.BinaryenNotVec128
OrInt32 = lib.BinaryenOrInt32
OrInt64 = lib.BinaryenOrInt64
OrVec128 = lib.BinaryenOrVec128
PMaxVecF32x4 = lib.BinaryenPMaxVecF32x4
PMaxVecF64x2 = lib.BinaryenPMaxVecF64x2
PMinVecF32x4 = lib.BinaryenPMinVecF32x4
PMinVecF64x2 = lib.BinaryenPMinVecF64x2
Pop = lib.BinaryenPop
PopId = lib.BinaryenPopId
PopcntInt32 = lib.BinaryenPopcntInt32
PopcntInt64 = lib.BinaryenPopcntInt64
PromoteFloat32 = lib.BinaryenPromoteFloat32
Push = lib.BinaryenPush
PushGetValue = lib.BinaryenPushGetValue
PushId = lib.BinaryenPushId
QFMAVecF32x4 = lib.BinaryenQFMAVecF32x4
QFMAVecF64x2 = lib.BinaryenQFMAVecF64x2
QFMSVecF32x4 = lib.BinaryenQFMSVecF32x4
QFMSVecF64x2 = lib.BinaryenQFMSVecF64x2
RefFunc = lib.BinaryenRefFunc
RefFuncGetFunc = lib.BinaryenRefFuncGetFunc
RefFuncId = lib.BinaryenRefFuncId
RefIsNull = lib.BinaryenRefIsNull
RefIsNullGetValue = lib.BinaryenRefIsNullGetValue
RefIsNullId = lib.BinaryenRefIsNullId
RefNull = lib.BinaryenRefNull
RefNullId = lib.BinaryenRefNullId
ReinterpretFloat32 = lib.BinaryenReinterpretFloat32
ReinterpretFloat64 = lib.BinaryenReinterpretFloat64
ReinterpretInt32 = lib.BinaryenReinterpretInt32
ReinterpretInt64 = lib.BinaryenReinterpretInt64
RemSInt32 = lib.BinaryenRemSInt32
RemSInt64 = lib.BinaryenRemSInt64
RemUInt32 = lib.BinaryenRemUInt32
RemUInt64 = lib.BinaryenRemUInt64
RemoveEvent = lib.BinaryenRemoveEvent
RemoveExport = lib.BinaryenRemoveExport
RemoveFunction = lib.BinaryenRemoveFunction
RemoveGlobal = lib.BinaryenRemoveGlobal
ReplaceLaneVecF32x4 = lib.BinaryenReplaceLaneVecF32x4
ReplaceLaneVecF64x2 = lib.BinaryenReplaceLaneVecF64x2
ReplaceLaneVecI16x8 = lib.BinaryenReplaceLaneVecI16x8
ReplaceLaneVecI32x4 = lib.BinaryenReplaceLaneVecI32x4
ReplaceLaneVecI64x2 = lib.BinaryenReplaceLaneVecI64x2
ReplaceLaneVecI8x16 = lib.BinaryenReplaceLaneVecI8x16
Rethrow = lib.BinaryenRethrow
RethrowGetExnref = lib.BinaryenRethrowGetExnref
RethrowId = lib.BinaryenRethrowId
Return = lib.BinaryenReturn
ReturnCall = lib.BinaryenReturnCall
ReturnCallIndirect = lib.BinaryenReturnCallIndirect
ReturnGetValue = lib.BinaryenReturnGetValue
ReturnId = lib.BinaryenReturnId
RotLInt32 = lib.BinaryenRotLInt32
RotLInt64 = lib.BinaryenRotLInt64
RotRInt32 = lib.BinaryenRotRInt32
RotRInt64 = lib.BinaryenRotRInt64
SIMDExtract = lib.BinaryenSIMDExtract
SIMDExtractGetIndex = lib.BinaryenSIMDExtractGetIndex
SIMDExtractGetOp = lib.BinaryenSIMDExtractGetOp
SIMDExtractGetVec = lib.BinaryenSIMDExtractGetVec
SIMDExtractId = lib.BinaryenSIMDExtractId
SIMDLoad = lib.BinaryenSIMDLoad
SIMDLoadGetAlign = lib.BinaryenSIMDLoadGetAlign
SIMDLoadGetOffset = lib.BinaryenSIMDLoadGetOffset
SIMDLoadGetOp = lib.BinaryenSIMDLoadGetOp
SIMDLoadGetPtr = lib.BinaryenSIMDLoadGetPtr
SIMDLoadId = lib.BinaryenSIMDLoadId
SIMDReplace = lib.BinaryenSIMDReplace
SIMDReplaceGetIndex = lib.BinaryenSIMDReplaceGetIndex
SIMDReplaceGetOp = lib.BinaryenSIMDReplaceGetOp
SIMDReplaceGetValue = lib.BinaryenSIMDReplaceGetValue
SIMDReplaceGetVec = lib.BinaryenSIMDReplaceGetVec
SIMDReplaceId = lib.BinaryenSIMDReplaceId
SIMDShift = lib.BinaryenSIMDShift
SIMDShiftGetOp = lib.BinaryenSIMDShiftGetOp
SIMDShiftGetShift = lib.BinaryenSIMDShiftGetShift
SIMDShiftGetVec = lib.BinaryenSIMDShiftGetVec
SIMDShiftId = lib.BinaryenSIMDShiftId
SIMDShuffle = lib.BinaryenSIMDShuffle
SIMDShuffleGetLeft = lib.BinaryenSIMDShuffleGetLeft
SIMDShuffleGetMask = lib.BinaryenSIMDShuffleGetMask
SIMDShuffleGetRight = lib.BinaryenSIMDShuffleGetRight
SIMDShuffleId = lib.BinaryenSIMDShuffleId
SIMDTernary = lib.BinaryenSIMDTernary
SIMDTernaryGetA = lib.BinaryenSIMDTernaryGetA
SIMDTernaryGetB = lib.BinaryenSIMDTernaryGetB
SIMDTernaryGetC = lib.BinaryenSIMDTernaryGetC
SIMDTernaryGetOp = lib.BinaryenSIMDTernaryGetOp
SIMDTernaryId = lib.BinaryenSIMDTernaryId
Select = lib.BinaryenSelect
SelectGetCondition = lib.BinaryenSelectGetCondition
SelectGetIfFalse = lib.BinaryenSelectGetIfFalse
SelectGetIfTrue = lib.BinaryenSelectGetIfTrue
SelectId = lib.BinaryenSelectId
SetAlwaysInlineMaxSize = lib.BinaryenSetAlwaysInlineMaxSize
SetColorsEnabled = lib.BinaryenSetColorsEnabled
SetDebugInfo = lib.BinaryenSetDebugInfo
SetFlexibleInlineMaxSize = lib.BinaryenSetFlexibleInlineMaxSize
SetFunctionTable = lib.BinaryenSetFunctionTable
SetLowMemoryUnused = lib.BinaryenSetLowMemoryUnused
SetMemory = lib.BinaryenSetMemory
SetOneCallerInlineMaxSize = lib.BinaryenSetOneCallerInlineMaxSize
SetOptimizeLevel = lib.BinaryenSetOptimizeLevel
SetPassArgument = lib.BinaryenSetPassArgument
SetShrinkLevel = lib.BinaryenSetShrinkLevel
SetStart = lib.BinaryenSetStart
ShlInt32 = lib.BinaryenShlInt32
ShlInt64 = lib.BinaryenShlInt64
ShlVecI16x8 = lib.BinaryenShlVecI16x8
ShlVecI32x4 = lib.BinaryenShlVecI32x4
ShlVecI64x2 = lib.BinaryenShlVecI64x2
ShlVecI8x16 = lib.BinaryenShlVecI8x16
ShrSInt32 = lib.BinaryenShrSInt32
ShrSInt64 = lib.BinaryenShrSInt64
ShrSVecI16x8 = lib.BinaryenShrSVecI16x8
ShrSVecI32x4 = lib.BinaryenShrSVecI32x4
ShrSVecI64x2 = lib.BinaryenShrSVecI64x2
ShrSVecI8x16 = lib.BinaryenShrSVecI8x16
ShrUInt32 = lib.BinaryenShrUInt32
ShrUInt64 = lib.BinaryenShrUInt64
ShrUVecI16x8 = lib.BinaryenShrUVecI16x8
ShrUVecI32x4 = lib.BinaryenShrUVecI32x4
ShrUVecI64x2 = lib.BinaryenShrUVecI64x2
ShrUVecI8x16 = lib.BinaryenShrUVecI8x16
SideEffectAny = lib.BinaryenSideEffectAny
SideEffectBranches = lib.BinaryenSideEffectBranches
SideEffectCalls = lib.BinaryenSideEffectCalls
SideEffectImplicitTrap = lib.BinaryenSideEffectImplicitTrap
SideEffectIsAtomic = lib.BinaryenSideEffectIsAtomic
SideEffectNone = lib.BinaryenSideEffectNone
SideEffectReadsGlobal = lib.BinaryenSideEffectReadsGlobal
SideEffectReadsLocal = lib.BinaryenSideEffectReadsLocal
SideEffectReadsMemory = lib.BinaryenSideEffectReadsMemory
SideEffectThrows = lib.BinaryenSideEffectThrows
SideEffectWritesGlobal = lib.BinaryenSideEffectWritesGlobal
SideEffectWritesLocal = lib.BinaryenSideEffectWritesLocal
SideEffectWritesMemory = lib.BinaryenSideEffectWritesMemory
SplatVecF32x4 = lib.BinaryenSplatVecF32x4
SplatVecF64x2 = lib.BinaryenSplatVecF64x2
SplatVecI16x8 = lib.BinaryenSplatVecI16x8
SplatVecI32x4 = lib.BinaryenSplatVecI32x4
SplatVecI64x2 = lib.BinaryenSplatVecI64x2
SplatVecI8x16 = lib.BinaryenSplatVecI8x16
SqrtFloat32 = lib.BinaryenSqrtFloat32
SqrtFloat64 = lib.BinaryenSqrtFloat64
SqrtVecF32x4 = lib.BinaryenSqrtVecF32x4
SqrtVecF64x2 = lib.BinaryenSqrtVecF64x2
Store = lib.BinaryenStore
StoreGetAlign = lib.BinaryenStoreGetAlign
StoreGetBytes = lib.BinaryenStoreGetBytes
StoreGetOffset = lib.BinaryenStoreGetOffset
StoreGetPtr = lib.BinaryenStoreGetPtr
StoreGetValue = lib.BinaryenStoreGetValue
StoreId = lib.BinaryenStoreId
StoreIsAtomic = lib.BinaryenStoreIsAtomic
SubFloat32 = lib.BinaryenSubFloat32
SubFloat64 = lib.BinaryenSubFloat64
SubInt32 = lib.BinaryenSubInt32
SubInt64 = lib.BinaryenSubInt64
SubSatSVecI16x8 = lib.BinaryenSubSatSVecI16x8
SubSatSVecI8x16 = lib.BinaryenSubSatSVecI8x16
SubSatUVecI16x8 = lib.BinaryenSubSatUVecI16x8
SubSatUVecI8x16 = lib.BinaryenSubSatUVecI8x16
SubVecF32x4 = lib.BinaryenSubVecF32x4
SubVecF64x2 = lib.BinaryenSubVecF64x2
SubVecI16x8 = lib.BinaryenSubVecI16x8
SubVecI32x4 = lib.BinaryenSubVecI32x4
SubVecI64x2 = lib.BinaryenSubVecI64x2
SubVecI8x16 = lib.BinaryenSubVecI8x16
Switch = lib.BinaryenSwitch
SwitchGetCondition = lib.BinaryenSwitchGetCondition
SwitchGetDefaultName = lib.BinaryenSwitchGetDefaultName
SwitchGetName = lib.BinaryenSwitchGetName
SwitchGetNumNames = lib.BinaryenSwitchGetNumNames
SwitchGetValue = lib.BinaryenSwitchGetValue
SwitchId = lib.BinaryenSwitchId
SwizzleVec8x16 = lib.BinaryenSwizzleVec8x16
Throw = lib.BinaryenThrow
ThrowGetEvent = lib.BinaryenThrowGetEvent
ThrowGetNumOperands = lib.BinaryenThrowGetNumOperands
ThrowGetOperand = lib.BinaryenThrowGetOperand
ThrowId = lib.BinaryenThrowId
TruncFloat32 = lib.BinaryenTruncFloat32
TruncFloat64 = lib.BinaryenTruncFloat64
TruncSFloat32ToInt32 = lib.BinaryenTruncSFloat32ToInt32
TruncSFloat32ToInt64 = lib.BinaryenTruncSFloat32ToInt64
TruncSFloat64ToInt32 = lib.BinaryenTruncSFloat64ToInt32
TruncSFloat64ToInt64 = lib.BinaryenTruncSFloat64ToInt64
TruncSatSFloat32ToInt32 = lib.BinaryenTruncSatSFloat32ToInt32
TruncSatSFloat32ToInt64 = lib.BinaryenTruncSatSFloat32ToInt64
TruncSatSFloat64ToInt32 = lib.BinaryenTruncSatSFloat64ToInt32
TruncSatSFloat64ToInt64 = lib.BinaryenTruncSatSFloat64ToInt64
TruncSatSVecF32x4ToVecI32x4 = lib.BinaryenTruncSatSVecF32x4ToVecI32x4
TruncSatSVecF64x2ToVecI64x2 = lib.BinaryenTruncSatSVecF64x2ToVecI64x2
TruncSatUFloat32ToInt32 = lib.BinaryenTruncSatUFloat32ToInt32
TruncSatUFloat32ToInt64 = lib.BinaryenTruncSatUFloat32ToInt64
TruncSatUFloat64ToInt32 = lib.BinaryenTruncSatUFloat64ToInt32
TruncSatUFloat64ToInt64 = lib.BinaryenTruncSatUFloat64ToInt64
TruncSatUVecF32x4ToVecI32x4 = lib.BinaryenTruncSatUVecF32x4ToVecI32x4
TruncSatUVecF64x2ToVecI64x2 = lib.BinaryenTruncSatUVecF64x2ToVecI64x2
TruncUFloat32ToInt32 = lib.BinaryenTruncUFloat32ToInt32
TruncUFloat32ToInt64 = lib.BinaryenTruncUFloat32ToInt64
TruncUFloat64ToInt32 = lib.BinaryenTruncUFloat64ToInt32
TruncUFloat64ToInt64 = lib.BinaryenTruncUFloat64ToInt64
Try = lib.BinaryenTry
TryGetBody = lib.BinaryenTryGetBody
TryGetCatchBody = lib.BinaryenTryGetCatchBody
TryId = lib.BinaryenTryId
TupleExtract = lib.BinaryenTupleExtract
TupleExtractGetIndex = lib.BinaryenTupleExtractGetIndex
TupleExtractGetTuple = lib.BinaryenTupleExtractGetTuple
TupleExtractId = lib.BinaryenTupleExtractId
TupleMake = lib.BinaryenTupleMake
TupleMakeGetNumOperands = lib.BinaryenTupleMakeGetNumOperands
TupleMakeGetOperand = lib.BinaryenTupleMakeGetOperand
TupleMakeId = lib.BinaryenTupleMakeId
TypeAnyref = lib.BinaryenTypeAnyref
TypeArity = lib.BinaryenTypeArity
TypeAuto = lib.BinaryenTypeAuto
TypeCreate = lib.BinaryenTypeCreate
TypeExnref = lib.BinaryenTypeExnref
TypeExpand = lib.BinaryenTypeExpand
TypeFloat32 = lib.BinaryenTypeFloat32
TypeFloat64 = lib.BinaryenTypeFloat64
TypeFuncref = lib.BinaryenTypeFuncref
TypeInt32 = lib.BinaryenTypeInt32
TypeInt64 = lib.BinaryenTypeInt64
TypeNone = lib.BinaryenTypeNone
TypeNullref = lib.BinaryenTypeNullref
TypeUnreachable = lib.BinaryenTypeUnreachable
TypeVec128 = lib.BinaryenTypeVec128
Unary = lib.BinaryenUnary
UnaryGetOp = lib.BinaryenUnaryGetOp
UnaryGetValue = lib.BinaryenUnaryGetValue
UnaryId = lib.BinaryenUnaryId
Unreachable = lib.BinaryenUnreachable
UnreachableId = lib.BinaryenUnreachableId
WidenHighSVecI16x8ToVecI32x4 = lib.BinaryenWidenHighSVecI16x8ToVecI32x4
WidenHighSVecI8x16ToVecI16x8 = lib.BinaryenWidenHighSVecI8x16ToVecI16x8
WidenHighUVecI16x8ToVecI32x4 = lib.BinaryenWidenHighUVecI16x8ToVecI32x4
WidenHighUVecI8x16ToVecI16x8 = lib.BinaryenWidenHighUVecI8x16ToVecI16x8
WidenLowSVecI16x8ToVecI32x4 = lib.BinaryenWidenLowSVecI16x8ToVecI32x4
WidenLowSVecI8x16ToVecI16x8 = lib.BinaryenWidenLowSVecI8x16ToVecI16x8
WidenLowUVecI16x8ToVecI32x4 = lib.BinaryenWidenLowUVecI16x8ToVecI32x4
WidenLowUVecI8x16ToVecI16x8 = lib.BinaryenWidenLowUVecI8x16ToVecI16x8
WrapInt64 = lib.BinaryenWrapInt64
XorInt32 = lib.BinaryenXorInt32
XorInt64 = lib.BinaryenXorInt64
XorVec128 = lib.BinaryenXorVec128
ExpressionRunnerCreate = lib.ExpressionRunnerCreate
ExpressionRunnerFlagsDefault = lib.ExpressionRunnerFlagsDefault
ExpressionRunnerFlagsPreserveSideeffects = lib.ExpressionRunnerFlagsPreserveSideeffects
ExpressionRunnerFlagsTraverseCalls = lib.ExpressionRunnerFlagsTraverseCalls
ExpressionRunnerRunAndDispose = lib.ExpressionRunnerRunAndDispose
ExpressionRunnerSetGlobalValue = lib.ExpressionRunnerSetGlobalValue
ExpressionRunnerSetLocalValue = lib.ExpressionRunnerSetLocalValue
RelooperAddBlock = lib.RelooperAddBlock
RelooperAddBlockWithSwitch = lib.RelooperAddBlockWithSwitch
RelooperAddBranch = lib.RelooperAddBranch
RelooperAddBranchForSwitch = lib.RelooperAddBranchForSwitch
RelooperCreate = lib.RelooperCreate
RelooperRenderAndDispose = lib.RelooperRenderAndDispose
