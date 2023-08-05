import datetime
import operator
import warnings
import numba
import numpy as np
import pandas as pd
from llvmlite import ir as lir
from numba.core import cgutils, types
from numba.core.imputils import impl_ret_new_ref, lower_constant
from numba.core.typing.templates import AttributeTemplate, signature
from numba.extending import NativeValue, box, infer_getattr, intrinsic, lower_builtin, lower_cast, make_attribute_wrapper, models, overload, overload_attribute, overload_method, register_jitable, register_model, typeof_impl, unbox
from numba.parfors.array_analysis import ArrayAnalysis
import bodo
import bodo.hiframes
import bodo.utils.conversion
from bodo.hiframes.datetime_timedelta_ext import pd_timedelta_type
from bodo.hiframes.pd_multi_index_ext import MultiIndexType
from bodo.hiframes.pd_series_ext import SeriesType
from bodo.hiframes.pd_timestamp_ext import pd_timestamp_type
from bodo.libs.binary_arr_ext import binary_array_type, bytes_type
from bodo.libs.bool_arr_ext import boolean_array
from bodo.libs.int_arr_ext import IntegerArrayType
from bodo.libs.pd_datetime_arr_ext import DatetimeArrayType
from bodo.libs.str_arr_ext import string_array_type
from bodo.libs.str_ext import string_type
from bodo.utils.transform import get_const_func_output_type
from bodo.utils.typing import BodoError, ColNamesMetaType, check_unsupported_args, create_unsupported_overload, dtype_to_array_type, get_overload_const_func, get_overload_const_int, get_overload_const_list, get_overload_const_str, get_overload_const_tuple, get_udf_error_msg, get_udf_out_arr_type, get_val_type_maybe_str_literal, is_const_func_type, is_heterogeneous_tuple_type, is_iterable_type, is_overload_bool, is_overload_constant_int, is_overload_constant_list, is_overload_constant_nan, is_overload_constant_str, is_overload_constant_tuple, is_overload_false, is_overload_none, is_overload_true, is_str_arr_type, parse_dtype, raise_bodo_error
from bodo.utils.utils import is_null_value
_dt_index_data_typ = types.Array(types.NPDatetime('ns'), 1, 'C')
_timedelta_index_data_typ = types.Array(types.NPTimedelta('ns'), 1, 'C')
iNaT = pd._libs.tslibs.iNaT
NaT = types.NPDatetime('ns')('NaT')
idx_cpy_arg_defaults = dict(deep=False, dtype=None, names=None)
idx_typ_to_format_str_map = dict()


@typeof_impl.register(pd.Index)
def typeof_pd_index(val, c):
    if val.inferred_type == 'string' or pd._libs.lib.infer_dtype(val, True
        ) == 'string':
        return StringIndexType(get_val_type_maybe_str_literal(val.name))
    if val.inferred_type == 'bytes' or pd._libs.lib.infer_dtype(val, True
        ) == 'bytes':
        return BinaryIndexType(get_val_type_maybe_str_literal(val.name))
    if val.equals(pd.Index([])):
        return StringIndexType(get_val_type_maybe_str_literal(val.name))
    if val.inferred_type == 'date':
        return DatetimeIndexType(get_val_type_maybe_str_literal(val.name))
    if val.inferred_type == 'integer' or pd._libs.lib.infer_dtype(val, True
        ) == 'integer':
        if isinstance(val.dtype, pd.core.arrays.integer._IntegerDtype):
            grlvw__kwdgw = val.dtype.numpy_dtype
            dtype = numba.np.numpy_support.from_dtype(grlvw__kwdgw)
        else:
            dtype = types.int64
        return NumericIndexType(dtype, get_val_type_maybe_str_literal(val.
            name), IntegerArrayType(dtype))
    if val.inferred_type == 'boolean' or pd._libs.lib.infer_dtype(val, True
        ) == 'boolean':
        return NumericIndexType(types.bool_, get_val_type_maybe_str_literal
            (val.name), boolean_array)
    raise NotImplementedError(f'unsupported pd.Index type {val}')


class DatetimeIndexType(types.IterableType, types.ArrayCompatible):

    def __init__(self, name_typ=None, data=None):
        name_typ = types.none if name_typ is None else name_typ
        self.name_typ = name_typ
        self.data = types.Array(bodo.datetime64ns, 1, 'C'
            ) if data is None else data
        super(DatetimeIndexType, self).__init__(name=
            f'DatetimeIndex({name_typ}, {self.data})')
    ndim = 1

    @property
    def as_array(self):
        return types.Array(types.undefined, 1, 'C')

    @property
    def dtype(self):
        return self.data.dtype

    @property
    def tzval(self):
        return self.data.tz if isinstance(self.data, bodo.DatetimeArrayType
            ) else None

    def copy(self):
        return DatetimeIndexType(self.name_typ, self.data)

    @property
    def iterator_type(self):
        return bodo.utils.typing.BodoArrayIterator(self, bodo.hiframes.
            pd_timestamp_ext.PandasTimestampType(self.tzval))

    @property
    def pandas_type_name(self):
        return self.data.dtype.type_name

    @property
    def numpy_type_name(self):
        return str(self.data.dtype)


types.datetime_index = DatetimeIndexType()


@typeof_impl.register(pd.DatetimeIndex)
def typeof_datetime_index(val, c):
    if isinstance(val.dtype, pd.DatetimeTZDtype):
        return DatetimeIndexType(get_val_type_maybe_str_literal(val.name),
            DatetimeArrayType(val.tz))
    return DatetimeIndexType(get_val_type_maybe_str_literal(val.name))


@register_model(DatetimeIndexType)
class DatetimeIndexModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        deo__qhjso = [('data', fe_type.data), ('name', fe_type.name_typ), (
            'dict', types.DictType(_dt_index_data_typ.dtype, types.int64))]
        super(DatetimeIndexModel, self).__init__(dmm, fe_type, deo__qhjso)


make_attribute_wrapper(DatetimeIndexType, 'data', '_data')
make_attribute_wrapper(DatetimeIndexType, 'name', '_name')
make_attribute_wrapper(DatetimeIndexType, 'dict', '_dict')


@overload_method(DatetimeIndexType, 'copy', no_unliteral=True)
def overload_datetime_index_copy(A, name=None, deep=False, dtype=None,
    names=None):
    pdqh__twc = dict(deep=deep, dtype=dtype, names=names)
    fyrwk__jmtv = idx_typ_to_format_str_map[DatetimeIndexType].format('copy()')
    check_unsupported_args('copy', pdqh__twc, idx_cpy_arg_defaults, fn_str=
        fyrwk__jmtv, package_name='pandas', module_name='Index')
    if not is_overload_none(name):

        def impl(A, name=None, deep=False, dtype=None, names=None):
            return bodo.hiframes.pd_index_ext.init_datetime_index(A._data.
                copy(), name)
    else:

        def impl(A, name=None, deep=False, dtype=None, names=None):
            return bodo.hiframes.pd_index_ext.init_datetime_index(A._data.
                copy(), A._name)
    return impl


@box(DatetimeIndexType)
def box_dt_index(typ, val, c):
    mxm__uztw = c.context.insert_const_string(c.builder.module, 'pandas')
    hdp__eos = c.pyapi.import_module_noblock(mxm__uztw)
    negp__quvlb = numba.core.cgutils.create_struct_proxy(typ)(c.context, c.
        builder, val)
    c.context.nrt.incref(c.builder, typ.data, negp__quvlb.data)
    uxp__qpe = c.pyapi.from_native_value(typ.data, negp__quvlb.data, c.
        env_manager)
    c.context.nrt.incref(c.builder, typ.name_typ, negp__quvlb.name)
    fyqru__rsm = c.pyapi.from_native_value(typ.name_typ, negp__quvlb.name,
        c.env_manager)
    args = c.pyapi.tuple_pack([uxp__qpe])
    txwyc__rhcf = c.pyapi.object_getattr_string(hdp__eos, 'DatetimeIndex')
    kws = c.pyapi.dict_pack([('name', fyqru__rsm)])
    plegg__ikob = c.pyapi.call(txwyc__rhcf, args, kws)
    c.pyapi.decref(uxp__qpe)
    c.pyapi.decref(fyqru__rsm)
    c.pyapi.decref(hdp__eos)
    c.pyapi.decref(txwyc__rhcf)
    c.pyapi.decref(args)
    c.pyapi.decref(kws)
    c.context.nrt.decref(c.builder, typ, val)
    return plegg__ikob


@unbox(DatetimeIndexType)
def unbox_datetime_index(typ, val, c):
    if isinstance(typ.data, DatetimeArrayType):
        jgeh__lwf = c.pyapi.object_getattr_string(val, 'array')
    else:
        jgeh__lwf = c.pyapi.object_getattr_string(val, 'values')
    data = c.pyapi.to_native_value(typ.data, jgeh__lwf).value
    fyqru__rsm = c.pyapi.object_getattr_string(val, 'name')
    name = c.pyapi.to_native_value(typ.name_typ, fyqru__rsm).value
    waftq__ihx = cgutils.create_struct_proxy(typ)(c.context, c.builder)
    waftq__ihx.data = data
    waftq__ihx.name = name
    dtype = _dt_index_data_typ.dtype
    awq__dix, urpk__nfmm = c.pyapi.call_jit_code(lambda : numba.typed.Dict.
        empty(dtype, types.int64), types.DictType(dtype, types.int64)(), [])
    waftq__ihx.dict = urpk__nfmm
    c.pyapi.decref(jgeh__lwf)
    c.pyapi.decref(fyqru__rsm)
    return NativeValue(waftq__ihx._getvalue())


@intrinsic
def init_datetime_index(typingctx, data, name):
    name = types.none if name is None else name

    def codegen(context, builder, signature, args):
        xeiw__gryez, nsgt__irg = args
        negp__quvlb = cgutils.create_struct_proxy(signature.return_type)(
            context, builder)
        negp__quvlb.data = xeiw__gryez
        negp__quvlb.name = nsgt__irg
        context.nrt.incref(builder, signature.args[0], xeiw__gryez)
        context.nrt.incref(builder, signature.args[1], nsgt__irg)
        dtype = _dt_index_data_typ.dtype
        negp__quvlb.dict = context.compile_internal(builder, lambda : numba
            .typed.Dict.empty(dtype, types.int64), types.DictType(dtype,
            types.int64)(), [])
        return negp__quvlb._getvalue()
    oblu__azmv = DatetimeIndexType(name, data)
    sig = signature(oblu__azmv, data, name)
    return sig, codegen


def init_index_equiv(self, scope, equiv_set, loc, args, kws):
    assert len(args) >= 1 and not kws
    qtsmd__ptmx = args[0]
    if equiv_set.has_shape(qtsmd__ptmx):
        return ArrayAnalysis.AnalyzeResult(shape=qtsmd__ptmx, pre=[])
    return None


(ArrayAnalysis._analyze_op_call_bodo_hiframes_pd_index_ext_init_datetime_index
    ) = init_index_equiv


def gen_dti_field_impl(field):
    ncl__uyeu = 'def impl(dti):\n'
    ncl__uyeu += '    numba.parfors.parfor.init_prange()\n'
    ncl__uyeu += '    A = bodo.hiframes.pd_index_ext.get_index_data(dti)\n'
    ncl__uyeu += '    name = bodo.hiframes.pd_index_ext.get_index_name(dti)\n'
    ncl__uyeu += '    n = len(A)\n'
    ncl__uyeu += '    S = np.empty(n, np.int64)\n'
    ncl__uyeu += '    for i in numba.parfors.parfor.internal_prange(n):\n'
    ncl__uyeu += '        val = A[i]\n'
    ncl__uyeu += '        ts = bodo.utils.conversion.box_if_dt64(val)\n'
    if field in ['weekday']:
        ncl__uyeu += '        S[i] = ts.' + field + '()\n'
    else:
        ncl__uyeu += '        S[i] = ts.' + field + '\n'
    ncl__uyeu += (
        '    return bodo.hiframes.pd_index_ext.init_numeric_index(S, name)\n')
    iqmgk__pwkj = {}
    exec(ncl__uyeu, {'numba': numba, 'np': np, 'bodo': bodo}, iqmgk__pwkj)
    impl = iqmgk__pwkj['impl']
    return impl


def _install_dti_date_fields():
    for field in bodo.hiframes.pd_timestamp_ext.date_fields:
        if field in ['is_leap_year']:
            continue
        impl = gen_dti_field_impl(field)
        overload_attribute(DatetimeIndexType, field)(lambda dti: impl)


_install_dti_date_fields()


@overload_attribute(DatetimeIndexType, 'is_leap_year')
def overload_datetime_index_is_leap_year(dti):

    def impl(dti):
        numba.parfors.parfor.init_prange()
        A = bodo.hiframes.pd_index_ext.get_index_data(dti)
        syi__wdj = len(A)
        S = np.empty(syi__wdj, np.bool_)
        for i in numba.parfors.parfor.internal_prange(syi__wdj):
            val = A[i]
            yblas__waw = bodo.utils.conversion.box_if_dt64(val)
            S[i] = bodo.hiframes.pd_timestamp_ext.is_leap_year(yblas__waw.year)
        return S
    return impl


@overload_attribute(DatetimeIndexType, 'date')
def overload_datetime_index_date(dti):

    def impl(dti):
        numba.parfors.parfor.init_prange()
        A = bodo.hiframes.pd_index_ext.get_index_data(dti)
        syi__wdj = len(A)
        S = bodo.hiframes.datetime_date_ext.alloc_datetime_date_array(syi__wdj)
        for i in numba.parfors.parfor.internal_prange(syi__wdj):
            val = A[i]
            yblas__waw = bodo.utils.conversion.box_if_dt64(val)
            S[i] = datetime.date(yblas__waw.year, yblas__waw.month,
                yblas__waw.day)
        return S
    return impl


@numba.njit(no_cpython_wrapper=True)
def _dti_val_finalize(s, count):
    if not count:
        s = iNaT
    return bodo.hiframes.pd_timestamp_ext.convert_datetime64_to_timestamp(s)


@numba.njit(no_cpython_wrapper=True)
def _tdi_val_finalize(s, count):
    return pd.Timedelta('nan') if not count else pd.Timedelta(s)


@overload_method(DatetimeIndexType, 'min', no_unliteral=True)
def overload_datetime_index_min(dti, axis=None, skipna=True):
    grdlp__pza = dict(axis=axis, skipna=skipna)
    bdenf__mso = dict(axis=None, skipna=True)
    check_unsupported_args('DatetimeIndex.min', grdlp__pza, bdenf__mso,
        package_name='pandas', module_name='Index')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(dti,
        'Index.min()')

    def impl(dti, axis=None, skipna=True):
        numba.parfors.parfor.init_prange()
        nbekt__nyct = bodo.hiframes.pd_index_ext.get_index_data(dti)
        s = numba.cpython.builtins.get_type_max_value(numba.core.types.int64)
        count = 0
        for i in numba.parfors.parfor.internal_prange(len(nbekt__nyct)):
            if not bodo.libs.array_kernels.isna(nbekt__nyct, i):
                val = bodo.hiframes.pd_timestamp_ext.dt64_to_integer(
                    nbekt__nyct[i])
                s = min(s, val)
                count += 1
        return bodo.hiframes.pd_index_ext._dti_val_finalize(s, count)
    return impl


@overload_method(DatetimeIndexType, 'max', no_unliteral=True)
def overload_datetime_index_max(dti, axis=None, skipna=True):
    grdlp__pza = dict(axis=axis, skipna=skipna)
    bdenf__mso = dict(axis=None, skipna=True)
    check_unsupported_args('DatetimeIndex.max', grdlp__pza, bdenf__mso,
        package_name='pandas', module_name='Index')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(dti,
        'Index.max()')

    def impl(dti, axis=None, skipna=True):
        numba.parfors.parfor.init_prange()
        nbekt__nyct = bodo.hiframes.pd_index_ext.get_index_data(dti)
        s = numba.cpython.builtins.get_type_min_value(numba.core.types.int64)
        count = 0
        for i in numba.parfors.parfor.internal_prange(len(nbekt__nyct)):
            if not bodo.libs.array_kernels.isna(nbekt__nyct, i):
                val = bodo.hiframes.pd_timestamp_ext.dt64_to_integer(
                    nbekt__nyct[i])
                s = max(s, val)
                count += 1
        return bodo.hiframes.pd_index_ext._dti_val_finalize(s, count)
    return impl


@overload_method(DatetimeIndexType, 'tz_convert', no_unliteral=True)
def overload_pd_datetime_tz_convert(A, tz):

    def impl(A, tz):
        return init_datetime_index(A._data.tz_convert(tz), A._name)
    return impl


@infer_getattr
class DatetimeIndexAttribute(AttributeTemplate):
    key = DatetimeIndexType

    def resolve_values(self, ary):
        return _dt_index_data_typ


@overload(pd.DatetimeIndex, no_unliteral=True)
def pd_datetimeindex_overload(data=None, freq=None, tz=None, normalize=
    False, closed=None, ambiguous='raise', dayfirst=False, yearfirst=False,
    dtype=None, copy=False, name=None):
    if is_overload_none(data):
        raise BodoError('data argument in pd.DatetimeIndex() expected')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(data,
        'pandas.DatetimeIndex()')
    grdlp__pza = dict(freq=freq, tz=tz, normalize=normalize, closed=closed,
        ambiguous=ambiguous, dayfirst=dayfirst, yearfirst=yearfirst, dtype=
        dtype, copy=copy)
    bdenf__mso = dict(freq=None, tz=None, normalize=False, closed=None,
        ambiguous='raise', dayfirst=False, yearfirst=False, dtype=None,
        copy=False)
    check_unsupported_args('pandas.DatetimeIndex', grdlp__pza, bdenf__mso,
        package_name='pandas', module_name='Index')

    def f(data=None, freq=None, tz=None, normalize=False, closed=None,
        ambiguous='raise', dayfirst=False, yearfirst=False, dtype=None,
        copy=False, name=None):
        tif__bqq = bodo.utils.conversion.coerce_to_array(data)
        S = bodo.utils.conversion.convert_to_dt64ns(tif__bqq)
        return bodo.hiframes.pd_index_ext.init_datetime_index(S, name)
    return f


def overload_sub_operator_datetime_index(lhs, rhs):
    if isinstance(lhs, DatetimeIndexType
        ) and rhs == bodo.hiframes.pd_timestamp_ext.pd_timestamp_type:
        wsw__jfevk = np.dtype('timedelta64[ns]')

        def impl(lhs, rhs):
            numba.parfors.parfor.init_prange()
            nbekt__nyct = bodo.hiframes.pd_index_ext.get_index_data(lhs)
            name = bodo.hiframes.pd_index_ext.get_index_name(lhs)
            syi__wdj = len(nbekt__nyct)
            S = np.empty(syi__wdj, wsw__jfevk)
            bbpzx__frec = rhs.value
            for i in numba.parfors.parfor.internal_prange(syi__wdj):
                S[i] = bodo.hiframes.pd_timestamp_ext.integer_to_timedelta64(
                    bodo.hiframes.pd_timestamp_ext.dt64_to_integer(
                    nbekt__nyct[i]) - bbpzx__frec)
            return bodo.hiframes.pd_index_ext.init_timedelta_index(S, name)
        return impl
    if isinstance(rhs, DatetimeIndexType
        ) and lhs == bodo.hiframes.pd_timestamp_ext.pd_timestamp_type:
        wsw__jfevk = np.dtype('timedelta64[ns]')

        def impl(lhs, rhs):
            numba.parfors.parfor.init_prange()
            nbekt__nyct = bodo.hiframes.pd_index_ext.get_index_data(rhs)
            name = bodo.hiframes.pd_index_ext.get_index_name(rhs)
            syi__wdj = len(nbekt__nyct)
            S = np.empty(syi__wdj, wsw__jfevk)
            bbpzx__frec = lhs.value
            for i in numba.parfors.parfor.internal_prange(syi__wdj):
                S[i] = bodo.hiframes.pd_timestamp_ext.integer_to_timedelta64(
                    bbpzx__frec - bodo.hiframes.pd_timestamp_ext.
                    dt64_to_integer(nbekt__nyct[i]))
            return bodo.hiframes.pd_index_ext.init_timedelta_index(S, name)
        return impl


def gen_dti_str_binop_impl(op, is_lhs_dti):
    qxj__gknfe = numba.core.utils.OPERATORS_TO_BUILTINS[op]
    ncl__uyeu = 'def impl(lhs, rhs):\n'
    if is_lhs_dti:
        ncl__uyeu += '  dt_index, _str = lhs, rhs\n'
        eynb__dmmsc = 'arr[i] {} other'.format(qxj__gknfe)
    else:
        ncl__uyeu += '  dt_index, _str = rhs, lhs\n'
        eynb__dmmsc = 'other {} arr[i]'.format(qxj__gknfe)
    ncl__uyeu += (
        '  arr = bodo.hiframes.pd_index_ext.get_index_data(dt_index)\n')
    ncl__uyeu += '  l = len(arr)\n'
    ncl__uyeu += (
        '  other = bodo.hiframes.pd_timestamp_ext.parse_datetime_str(_str)\n')
    ncl__uyeu += '  S = bodo.libs.bool_arr_ext.alloc_bool_array(l)\n'
    ncl__uyeu += '  for i in numba.parfors.parfor.internal_prange(l):\n'
    ncl__uyeu += '    S[i] = {}\n'.format(eynb__dmmsc)
    ncl__uyeu += '  return S\n'
    iqmgk__pwkj = {}
    exec(ncl__uyeu, {'bodo': bodo, 'numba': numba, 'np': np}, iqmgk__pwkj)
    impl = iqmgk__pwkj['impl']
    return impl


def overload_binop_dti_str(op):

    def overload_impl(lhs, rhs):
        if isinstance(lhs, DatetimeIndexType) and types.unliteral(rhs
            ) == string_type:
            return gen_dti_str_binop_impl(op, True)
        if isinstance(rhs, DatetimeIndexType) and types.unliteral(lhs
            ) == string_type:
            return gen_dti_str_binop_impl(op, False)
    return overload_impl


@overload(pd.Index, inline='always', no_unliteral=True)
def pd_index_overload(data=None, dtype=None, copy=False, name=None,
    tupleize_cols=True):
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(data,
        'pandas.Index()')
    data = types.unliteral(data) if not isinstance(data, types.LiteralList
        ) else data
    if not is_overload_none(dtype):
        zxku__pxio = parse_dtype(dtype, 'pandas.Index')
        vejr__vose = False
    else:
        zxku__pxio = getattr(data, 'dtype', None)
        vejr__vose = True
    if isinstance(zxku__pxio, types.misc.PyObject):
        raise BodoError(
            "pd.Index() object 'dtype' is not specific enough for typing. Please provide a more exact type (e.g. str)."
            )
    if isinstance(data, RangeIndexType):

        def impl(data=None, dtype=None, copy=False, name=None,
            tupleize_cols=True):
            return pd.RangeIndex(data, name=name)
    elif isinstance(data, DatetimeIndexType) or zxku__pxio == types.NPDatetime(
        'ns'):

        def impl(data=None, dtype=None, copy=False, name=None,
            tupleize_cols=True):
            return pd.DatetimeIndex(data, name=name)
    elif isinstance(data, TimedeltaIndexType
        ) or zxku__pxio == types.NPTimedelta('ns'):

        def impl(data=None, dtype=None, copy=False, name=None,
            tupleize_cols=True):
            return pd.TimedeltaIndex(data, name=name)
    elif is_heterogeneous_tuple_type(data):

        def impl(data=None, dtype=None, copy=False, name=None,
            tupleize_cols=True):
            return bodo.hiframes.pd_index_ext.init_heter_index(data, name)
        return impl
    elif bodo.utils.utils.is_array_typ(data, False) or isinstance(data, (
        SeriesType, types.List, types.UniTuple)):
        if isinstance(zxku__pxio, (types.Integer, types.Float, types.Boolean)):
            if vejr__vose:

                def impl(data=None, dtype=None, copy=False, name=None,
                    tupleize_cols=True):
                    tif__bqq = bodo.utils.conversion.coerce_to_array(data)
                    return bodo.hiframes.pd_index_ext.init_numeric_index(
                        tif__bqq, name)
            else:

                def impl(data=None, dtype=None, copy=False, name=None,
                    tupleize_cols=True):
                    tif__bqq = bodo.utils.conversion.coerce_to_array(data)
                    fuhtt__usj = bodo.utils.conversion.fix_arr_dtype(tif__bqq,
                        zxku__pxio)
                    return bodo.hiframes.pd_index_ext.init_numeric_index(
                        fuhtt__usj, name)
        elif zxku__pxio in [types.string, bytes_type]:

            def impl(data=None, dtype=None, copy=False, name=None,
                tupleize_cols=True):
                return bodo.hiframes.pd_index_ext.init_binary_str_index(bodo
                    .utils.conversion.coerce_to_array(data), name)
        else:
            raise BodoError(
                'pd.Index(): provided array is of unsupported type.')
    elif is_overload_none(data):
        raise BodoError(
            'data argument in pd.Index() is invalid: None or scalar is not acceptable'
            )
    else:
        raise BodoError(
            f'pd.Index(): the provided argument type {data} is not supported')
    return impl


@overload(operator.getitem, no_unliteral=True)
def overload_datetime_index_getitem(dti, ind):
    if isinstance(dti, DatetimeIndexType):
        if isinstance(ind, types.Integer):

            def impl(dti, ind):
                ajqnv__vxv = bodo.hiframes.pd_index_ext.get_index_data(dti)
                val = ajqnv__vxv[ind]
                return bodo.utils.conversion.box_if_dt64(val)
            return impl
        else:

            def impl(dti, ind):
                ajqnv__vxv = bodo.hiframes.pd_index_ext.get_index_data(dti)
                name = bodo.hiframes.pd_index_ext.get_index_name(dti)
                sfg__ojapp = ajqnv__vxv[ind]
                return bodo.hiframes.pd_index_ext.init_datetime_index(
                    sfg__ojapp, name)
            return impl


@overload(operator.getitem, no_unliteral=True)
def overload_timedelta_index_getitem(I, ind):
    if not isinstance(I, TimedeltaIndexType):
        return
    if isinstance(ind, types.Integer):

        def impl(I, ind):
            aogq__jmyl = bodo.hiframes.pd_index_ext.get_index_data(I)
            return pd.Timedelta(aogq__jmyl[ind])
        return impl

    def impl(I, ind):
        aogq__jmyl = bodo.hiframes.pd_index_ext.get_index_data(I)
        name = bodo.hiframes.pd_index_ext.get_index_name(I)
        sfg__ojapp = aogq__jmyl[ind]
        return bodo.hiframes.pd_index_ext.init_timedelta_index(sfg__ojapp, name
            )
    return impl


@overload(operator.getitem, no_unliteral=True)
def overload_categorical_index_getitem(I, ind):
    if not isinstance(I, CategoricalIndexType):
        return
    if isinstance(ind, types.Integer):

        def impl(I, ind):
            ygu__wpif = bodo.hiframes.pd_index_ext.get_index_data(I)
            val = ygu__wpif[ind]
            return val
        return impl
    if isinstance(ind, types.SliceType):

        def impl(I, ind):
            ygu__wpif = bodo.hiframes.pd_index_ext.get_index_data(I)
            name = bodo.hiframes.pd_index_ext.get_index_name(I)
            sfg__ojapp = ygu__wpif[ind]
            return bodo.hiframes.pd_index_ext.init_categorical_index(sfg__ojapp
                , name)
        return impl
    raise BodoError(
        f'pd.CategoricalIndex.__getitem__: unsupported index type {ind}')


@numba.njit(no_cpython_wrapper=True)
def validate_endpoints(closed):
    wdl__xrazj = False
    sokpq__ubm = False
    if closed is None:
        wdl__xrazj = True
        sokpq__ubm = True
    elif closed == 'left':
        wdl__xrazj = True
    elif closed == 'right':
        sokpq__ubm = True
    else:
        raise ValueError("Closed has to be either 'left', 'right' or None")
    return wdl__xrazj, sokpq__ubm


@numba.njit(no_cpython_wrapper=True)
def to_offset_value(freq):
    if freq is None:
        return None
    with numba.objmode(r='int64'):
        r = pd.tseries.frequencies.to_offset(freq).nanos
    return r


@numba.generated_jit(nopython=True, no_cpython_wrapper=True)
def _dummy_convert_none_to_int(val):
    if is_overload_none(val):

        def impl(val):
            return 0
        return impl
    if isinstance(val, types.Optional):

        def impl(val):
            if val is None:
                return 0
            return bodo.utils.indexing.unoptional(val)
        return impl
    return lambda val: val


@overload(pd.date_range, inline='always')
def pd_date_range_overload(start=None, end=None, periods=None, freq=None,
    tz=None, normalize=False, name=None, closed=None):
    grdlp__pza = dict(tz=tz, normalize=normalize, closed=closed)
    bdenf__mso = dict(tz=None, normalize=False, closed=None)
    check_unsupported_args('pandas.date_range', grdlp__pza, bdenf__mso,
        package_name='pandas', module_name='General')
    if not is_overload_none(tz):
        raise_bodo_error('pd.date_range(): tz argument not supported yet')
    xycq__pumoi = ''
    if is_overload_none(freq) and any(is_overload_none(t) for t in (start,
        end, periods)):
        freq = 'D'
        xycq__pumoi = "  freq = 'D'\n"
    if sum(not is_overload_none(t) for t in (start, end, periods, freq)) != 3:
        raise_bodo_error(
            'Of the four parameters: start, end, periods, and freq, exactly three must be specified'
            )
    ncl__uyeu = """def f(start=None, end=None, periods=None, freq=None, tz=None, normalize=False, name=None, closed=None):
"""
    ncl__uyeu += xycq__pumoi
    if is_overload_none(start):
        ncl__uyeu += "  start_t = pd.Timestamp('1800-01-03')\n"
    else:
        ncl__uyeu += '  start_t = pd.Timestamp(start)\n'
    if is_overload_none(end):
        ncl__uyeu += "  end_t = pd.Timestamp('1800-01-03')\n"
    else:
        ncl__uyeu += '  end_t = pd.Timestamp(end)\n'
    if not is_overload_none(freq):
        ncl__uyeu += (
            '  stride = bodo.hiframes.pd_index_ext.to_offset_value(freq)\n')
        if is_overload_none(periods):
            ncl__uyeu += '  b = start_t.value\n'
            ncl__uyeu += (
                '  e = b + (end_t.value - b) // stride * stride + stride // 2 + 1\n'
                )
        elif not is_overload_none(start):
            ncl__uyeu += '  b = start_t.value\n'
            ncl__uyeu += '  addend = np.int64(periods) * np.int64(stride)\n'
            ncl__uyeu += '  e = np.int64(b) + addend\n'
        elif not is_overload_none(end):
            ncl__uyeu += '  e = end_t.value + stride\n'
            ncl__uyeu += '  addend = np.int64(periods) * np.int64(-stride)\n'
            ncl__uyeu += '  b = np.int64(e) + addend\n'
        else:
            raise_bodo_error(
                "at least 'start' or 'end' should be specified if a 'period' is given."
                )
        ncl__uyeu += '  arr = np.arange(b, e, stride, np.int64)\n'
    else:
        ncl__uyeu += '  delta = end_t.value - start_t.value\n'
        ncl__uyeu += '  step = delta / (periods - 1)\n'
        ncl__uyeu += '  arr1 = np.arange(0, periods, 1, np.float64)\n'
        ncl__uyeu += '  arr1 *= step\n'
        ncl__uyeu += '  arr1 += start_t.value\n'
        ncl__uyeu += '  arr = arr1.astype(np.int64)\n'
        ncl__uyeu += '  arr[-1] = end_t.value\n'
    ncl__uyeu += '  A = bodo.utils.conversion.convert_to_dt64ns(arr)\n'
    ncl__uyeu += (
        '  return bodo.hiframes.pd_index_ext.init_datetime_index(A, name)\n')
    iqmgk__pwkj = {}
    exec(ncl__uyeu, {'bodo': bodo, 'np': np, 'pd': pd}, iqmgk__pwkj)
    f = iqmgk__pwkj['f']
    return f


@overload(pd.timedelta_range, no_unliteral=True)
def pd_timedelta_range_overload(start=None, end=None, periods=None, freq=
    None, name=None, closed=None):
    if is_overload_none(freq) and any(is_overload_none(t) for t in (start,
        end, periods)):
        freq = 'D'
    if sum(not is_overload_none(t) for t in (start, end, periods, freq)) != 3:
        raise BodoError(
            'Of the four parameters: start, end, periods, and freq, exactly three must be specified'
            )

    def f(start=None, end=None, periods=None, freq=None, name=None, closed=None
        ):
        if freq is None and (start is None or end is None or periods is None):
            freq = 'D'
        freq = bodo.hiframes.pd_index_ext.to_offset_value(freq)
        achf__rslh = pd.Timedelta('1 day')
        if start is not None:
            achf__rslh = pd.Timedelta(start)
        heavf__dys = pd.Timedelta('1 day')
        if end is not None:
            heavf__dys = pd.Timedelta(end)
        if start is None and end is None and closed is not None:
            raise ValueError(
                'Closed has to be None if not both of start and end are defined'
                )
        wdl__xrazj, sokpq__ubm = bodo.hiframes.pd_index_ext.validate_endpoints(
            closed)
        if freq is not None:
            mcc__dgzwc = _dummy_convert_none_to_int(freq)
            if periods is None:
                b = achf__rslh.value
                cvuwr__tqzq = b + (heavf__dys.value - b
                    ) // mcc__dgzwc * mcc__dgzwc + mcc__dgzwc // 2 + 1
            elif start is not None:
                periods = _dummy_convert_none_to_int(periods)
                b = achf__rslh.value
                lvbro__onmp = np.int64(periods) * np.int64(mcc__dgzwc)
                cvuwr__tqzq = np.int64(b) + lvbro__onmp
            elif end is not None:
                periods = _dummy_convert_none_to_int(periods)
                cvuwr__tqzq = heavf__dys.value + mcc__dgzwc
                lvbro__onmp = np.int64(periods) * np.int64(-mcc__dgzwc)
                b = np.int64(cvuwr__tqzq) + lvbro__onmp
            else:
                raise ValueError(
                    "at least 'start' or 'end' should be specified if a 'period' is given."
                    )
            owj__szc = np.arange(b, cvuwr__tqzq, mcc__dgzwc, np.int64)
        else:
            periods = _dummy_convert_none_to_int(periods)
            frmos__tix = heavf__dys.value - achf__rslh.value
            step = frmos__tix / (periods - 1)
            lrpg__vjq = np.arange(0, periods, 1, np.float64)
            lrpg__vjq *= step
            lrpg__vjq += achf__rslh.value
            owj__szc = lrpg__vjq.astype(np.int64)
            owj__szc[-1] = heavf__dys.value
        if not wdl__xrazj and len(owj__szc) and owj__szc[0
            ] == achf__rslh.value:
            owj__szc = owj__szc[1:]
        if not sokpq__ubm and len(owj__szc) and owj__szc[-1
            ] == heavf__dys.value:
            owj__szc = owj__szc[:-1]
        S = bodo.utils.conversion.convert_to_dt64ns(owj__szc)
        return bodo.hiframes.pd_index_ext.init_timedelta_index(S, name)
    return f


@overload_method(DatetimeIndexType, 'isocalendar', inline='always',
    no_unliteral=True)
def overload_pd_timestamp_isocalendar(idx):
    sgtsy__ebsge = ColNamesMetaType(('year', 'week', 'day'))

    def impl(idx):
        A = bodo.hiframes.pd_index_ext.get_index_data(idx)
        numba.parfors.parfor.init_prange()
        syi__wdj = len(A)
        cem__hrlf = bodo.libs.int_arr_ext.alloc_int_array(syi__wdj, np.uint32)
        dknq__qxu = bodo.libs.int_arr_ext.alloc_int_array(syi__wdj, np.uint32)
        ztojw__dmfs = bodo.libs.int_arr_ext.alloc_int_array(syi__wdj, np.uint32
            )
        for i in numba.parfors.parfor.internal_prange(syi__wdj):
            if bodo.libs.array_kernels.isna(A, i):
                bodo.libs.array_kernels.setna(cem__hrlf, i)
                bodo.libs.array_kernels.setna(dknq__qxu, i)
                bodo.libs.array_kernels.setna(ztojw__dmfs, i)
                continue
            cem__hrlf[i], dknq__qxu[i], ztojw__dmfs[i
                ] = bodo.utils.conversion.box_if_dt64(A[i]).isocalendar()
        return bodo.hiframes.pd_dataframe_ext.init_dataframe((cem__hrlf,
            dknq__qxu, ztojw__dmfs), idx, sgtsy__ebsge)
    return impl


class TimedeltaIndexType(types.IterableType, types.ArrayCompatible):

    def __init__(self, name_typ=None, data=None):
        name_typ = types.none if name_typ is None else name_typ
        self.name_typ = name_typ
        self.data = types.Array(bodo.timedelta64ns, 1, 'C'
            ) if data is None else data
        super(TimedeltaIndexType, self).__init__(name=
            f'TimedeltaIndexType({name_typ}, {self.data})')
    ndim = 1

    def copy(self):
        return TimedeltaIndexType(self.name_typ)

    @property
    def dtype(self):
        return types.NPTimedelta('ns')

    @property
    def as_array(self):
        return types.Array(types.undefined, 1, 'C')

    @property
    def key(self):
        return self.name_typ, self.data

    @property
    def iterator_type(self):
        return bodo.utils.typing.BodoArrayIterator(self, bodo.pd_timedelta_type
            )

    @property
    def pandas_type_name(self):
        return 'timedelta'

    @property
    def numpy_type_name(self):
        return 'timedelta64[ns]'


timedelta_index = TimedeltaIndexType()
types.timedelta_index = timedelta_index


@register_model(TimedeltaIndexType)
class TimedeltaIndexTypeModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        deo__qhjso = [('data', _timedelta_index_data_typ), ('name', fe_type
            .name_typ), ('dict', types.DictType(_timedelta_index_data_typ.
            dtype, types.int64))]
        super(TimedeltaIndexTypeModel, self).__init__(dmm, fe_type, deo__qhjso)


@typeof_impl.register(pd.TimedeltaIndex)
def typeof_timedelta_index(val, c):
    return TimedeltaIndexType(get_val_type_maybe_str_literal(val.name))


@box(TimedeltaIndexType)
def box_timedelta_index(typ, val, c):
    mxm__uztw = c.context.insert_const_string(c.builder.module, 'pandas')
    hdp__eos = c.pyapi.import_module_noblock(mxm__uztw)
    timedelta_index = numba.core.cgutils.create_struct_proxy(typ)(c.context,
        c.builder, val)
    c.context.nrt.incref(c.builder, _timedelta_index_data_typ,
        timedelta_index.data)
    uxp__qpe = c.pyapi.from_native_value(_timedelta_index_data_typ,
        timedelta_index.data, c.env_manager)
    c.context.nrt.incref(c.builder, typ.name_typ, timedelta_index.name)
    fyqru__rsm = c.pyapi.from_native_value(typ.name_typ, timedelta_index.
        name, c.env_manager)
    args = c.pyapi.tuple_pack([uxp__qpe])
    kws = c.pyapi.dict_pack([('name', fyqru__rsm)])
    txwyc__rhcf = c.pyapi.object_getattr_string(hdp__eos, 'TimedeltaIndex')
    plegg__ikob = c.pyapi.call(txwyc__rhcf, args, kws)
    c.pyapi.decref(uxp__qpe)
    c.pyapi.decref(fyqru__rsm)
    c.pyapi.decref(hdp__eos)
    c.pyapi.decref(txwyc__rhcf)
    c.pyapi.decref(args)
    c.pyapi.decref(kws)
    c.context.nrt.decref(c.builder, typ, val)
    return plegg__ikob


@unbox(TimedeltaIndexType)
def unbox_timedelta_index(typ, val, c):
    rhovc__ampy = c.pyapi.object_getattr_string(val, 'values')
    data = c.pyapi.to_native_value(_timedelta_index_data_typ, rhovc__ampy
        ).value
    fyqru__rsm = c.pyapi.object_getattr_string(val, 'name')
    name = c.pyapi.to_native_value(typ.name_typ, fyqru__rsm).value
    c.pyapi.decref(rhovc__ampy)
    c.pyapi.decref(fyqru__rsm)
    waftq__ihx = cgutils.create_struct_proxy(typ)(c.context, c.builder)
    waftq__ihx.data = data
    waftq__ihx.name = name
    dtype = _timedelta_index_data_typ.dtype
    awq__dix, urpk__nfmm = c.pyapi.call_jit_code(lambda : numba.typed.Dict.
        empty(dtype, types.int64), types.DictType(dtype, types.int64)(), [])
    waftq__ihx.dict = urpk__nfmm
    return NativeValue(waftq__ihx._getvalue())


@intrinsic
def init_timedelta_index(typingctx, data, name=None):
    name = types.none if name is None else name

    def codegen(context, builder, signature, args):
        xeiw__gryez, nsgt__irg = args
        timedelta_index = cgutils.create_struct_proxy(signature.return_type)(
            context, builder)
        timedelta_index.data = xeiw__gryez
        timedelta_index.name = nsgt__irg
        context.nrt.incref(builder, signature.args[0], xeiw__gryez)
        context.nrt.incref(builder, signature.args[1], nsgt__irg)
        dtype = _timedelta_index_data_typ.dtype
        timedelta_index.dict = context.compile_internal(builder, lambda :
            numba.typed.Dict.empty(dtype, types.int64), types.DictType(
            dtype, types.int64)(), [])
        return timedelta_index._getvalue()
    oblu__azmv = TimedeltaIndexType(name)
    sig = signature(oblu__azmv, data, name)
    return sig, codegen


(ArrayAnalysis._analyze_op_call_bodo_hiframes_pd_index_ext_init_timedelta_index
    ) = init_index_equiv


@infer_getattr
class TimedeltaIndexAttribute(AttributeTemplate):
    key = TimedeltaIndexType

    def resolve_values(self, ary):
        return _timedelta_index_data_typ


make_attribute_wrapper(TimedeltaIndexType, 'data', '_data')
make_attribute_wrapper(TimedeltaIndexType, 'name', '_name')
make_attribute_wrapper(TimedeltaIndexType, 'dict', '_dict')


@overload_method(TimedeltaIndexType, 'copy', no_unliteral=True)
def overload_timedelta_index_copy(A, name=None, deep=False, dtype=None,
    names=None):
    pdqh__twc = dict(deep=deep, dtype=dtype, names=names)
    fyrwk__jmtv = idx_typ_to_format_str_map[TimedeltaIndexType].format('copy()'
        )
    check_unsupported_args('TimedeltaIndex.copy', pdqh__twc,
        idx_cpy_arg_defaults, fn_str=fyrwk__jmtv, package_name='pandas',
        module_name='Index')
    if not is_overload_none(name):

        def impl(A, name=None, deep=False, dtype=None, names=None):
            return bodo.hiframes.pd_index_ext.init_timedelta_index(A._data.
                copy(), name)
    else:

        def impl(A, name=None, deep=False, dtype=None, names=None):
            return bodo.hiframes.pd_index_ext.init_timedelta_index(A._data.
                copy(), A._name)
    return impl


@overload_method(TimedeltaIndexType, 'min', inline='always', no_unliteral=True)
def overload_timedelta_index_min(tdi, axis=None, skipna=True):
    grdlp__pza = dict(axis=axis, skipna=skipna)
    bdenf__mso = dict(axis=None, skipna=True)
    check_unsupported_args('TimedeltaIndex.min', grdlp__pza, bdenf__mso,
        package_name='pandas', module_name='Index')

    def impl(tdi, axis=None, skipna=True):
        numba.parfors.parfor.init_prange()
        data = bodo.hiframes.pd_index_ext.get_index_data(tdi)
        syi__wdj = len(data)
        kefg__spuw = numba.cpython.builtins.get_type_max_value(numba.core.
            types.int64)
        count = 0
        for i in numba.parfors.parfor.internal_prange(syi__wdj):
            if bodo.libs.array_kernels.isna(data, i):
                continue
            val = (bodo.hiframes.datetime_timedelta_ext.
                cast_numpy_timedelta_to_int(data[i]))
            count += 1
            kefg__spuw = min(kefg__spuw, val)
        bzafw__wlu = bodo.hiframes.pd_timestamp_ext.integer_to_timedelta64(
            kefg__spuw)
        return bodo.hiframes.pd_index_ext._tdi_val_finalize(bzafw__wlu, count)
    return impl


@overload_method(TimedeltaIndexType, 'max', inline='always', no_unliteral=True)
def overload_timedelta_index_max(tdi, axis=None, skipna=True):
    grdlp__pza = dict(axis=axis, skipna=skipna)
    bdenf__mso = dict(axis=None, skipna=True)
    check_unsupported_args('TimedeltaIndex.max', grdlp__pza, bdenf__mso,
        package_name='pandas', module_name='Index')
    if not is_overload_none(axis) or not is_overload_true(skipna):
        raise BodoError(
            'Index.min(): axis and skipna arguments not supported yet')

    def impl(tdi, axis=None, skipna=True):
        numba.parfors.parfor.init_prange()
        data = bodo.hiframes.pd_index_ext.get_index_data(tdi)
        syi__wdj = len(data)
        pdtdx__kltt = numba.cpython.builtins.get_type_min_value(numba.core.
            types.int64)
        count = 0
        for i in numba.parfors.parfor.internal_prange(syi__wdj):
            if bodo.libs.array_kernels.isna(data, i):
                continue
            val = (bodo.hiframes.datetime_timedelta_ext.
                cast_numpy_timedelta_to_int(data[i]))
            count += 1
            pdtdx__kltt = max(pdtdx__kltt, val)
        bzafw__wlu = bodo.hiframes.pd_timestamp_ext.integer_to_timedelta64(
            pdtdx__kltt)
        return bodo.hiframes.pd_index_ext._tdi_val_finalize(bzafw__wlu, count)
    return impl


def gen_tdi_field_impl(field):
    ncl__uyeu = 'def impl(tdi):\n'
    ncl__uyeu += '    numba.parfors.parfor.init_prange()\n'
    ncl__uyeu += '    A = bodo.hiframes.pd_index_ext.get_index_data(tdi)\n'
    ncl__uyeu += '    name = bodo.hiframes.pd_index_ext.get_index_name(tdi)\n'
    ncl__uyeu += '    n = len(A)\n'
    ncl__uyeu += '    S = np.empty(n, np.int64)\n'
    ncl__uyeu += '    for i in numba.parfors.parfor.internal_prange(n):\n'
    ncl__uyeu += (
        '        td64 = bodo.hiframes.pd_timestamp_ext.timedelta64_to_integer(A[i])\n'
        )
    if field == 'nanoseconds':
        ncl__uyeu += '        S[i] = td64 % 1000\n'
    elif field == 'microseconds':
        ncl__uyeu += '        S[i] = td64 // 1000 % 100000\n'
    elif field == 'seconds':
        ncl__uyeu += (
            '        S[i] = td64 // (1000 * 1000000) % (60 * 60 * 24)\n')
    elif field == 'days':
        ncl__uyeu += '        S[i] = td64 // (1000 * 1000000 * 60 * 60 * 24)\n'
    else:
        assert False, 'invalid timedelta field'
    ncl__uyeu += (
        '    return bodo.hiframes.pd_index_ext.init_numeric_index(S, name)\n')
    iqmgk__pwkj = {}
    exec(ncl__uyeu, {'numba': numba, 'np': np, 'bodo': bodo}, iqmgk__pwkj)
    impl = iqmgk__pwkj['impl']
    return impl


def _install_tdi_time_fields():
    for field in bodo.hiframes.pd_timestamp_ext.timedelta_fields:
        impl = gen_tdi_field_impl(field)
        overload_attribute(TimedeltaIndexType, field)(lambda tdi: impl)


_install_tdi_time_fields()


@overload(pd.TimedeltaIndex, no_unliteral=True)
def pd_timedelta_index_overload(data=None, unit=None, freq=None, dtype=None,
    copy=False, name=None):
    if is_overload_none(data):
        raise BodoError('data argument in pd.TimedeltaIndex() expected')
    grdlp__pza = dict(unit=unit, freq=freq, dtype=dtype, copy=copy)
    bdenf__mso = dict(unit=None, freq=None, dtype=None, copy=False)
    check_unsupported_args('pandas.TimedeltaIndex', grdlp__pza, bdenf__mso,
        package_name='pandas', module_name='Index')

    def impl(data=None, unit=None, freq=None, dtype=None, copy=False, name=None
        ):
        tif__bqq = bodo.utils.conversion.coerce_to_array(data)
        S = bodo.utils.conversion.convert_to_td64ns(tif__bqq)
        return bodo.hiframes.pd_index_ext.init_timedelta_index(S, name)
    return impl


class RangeIndexType(types.IterableType, types.ArrayCompatible):

    def __init__(self, name_typ=None):
        if name_typ is None:
            name_typ = types.none
        self.name_typ = name_typ
        super(RangeIndexType, self).__init__(name=f'RangeIndexType({name_typ})'
            )
    ndim = 1

    @property
    def as_array(self):
        return types.Array(types.undefined, 1, 'C')

    def copy(self):
        return RangeIndexType(self.name_typ)

    @property
    def iterator_type(self):
        return types.iterators.RangeIteratorType(types.int64)

    @property
    def dtype(self):
        return types.int64

    @property
    def pandas_type_name(self):
        return str(self.dtype)

    @property
    def numpy_type_name(self):
        return str(self.dtype)

    def unify(self, typingctx, other):
        if isinstance(other, NumericIndexType):
            name_typ = self.name_typ.unify(typingctx, other.name_typ)
            if name_typ is None:
                name_typ = types.none
            return NumericIndexType(types.int64, name_typ)


@typeof_impl.register(pd.RangeIndex)
def typeof_pd_range_index(val, c):
    return RangeIndexType(get_val_type_maybe_str_literal(val.name))


@register_model(RangeIndexType)
class RangeIndexModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        deo__qhjso = [('start', types.int64), ('stop', types.int64), (
            'step', types.int64), ('name', fe_type.name_typ)]
        super(RangeIndexModel, self).__init__(dmm, fe_type, deo__qhjso)


make_attribute_wrapper(RangeIndexType, 'start', '_start')
make_attribute_wrapper(RangeIndexType, 'stop', '_stop')
make_attribute_wrapper(RangeIndexType, 'step', '_step')
make_attribute_wrapper(RangeIndexType, 'name', '_name')


@overload_method(RangeIndexType, 'copy', no_unliteral=True)
def overload_range_index_copy(A, name=None, deep=False, dtype=None, names=None
    ):
    pdqh__twc = dict(deep=deep, dtype=dtype, names=names)
    fyrwk__jmtv = idx_typ_to_format_str_map[RangeIndexType].format('copy()')
    check_unsupported_args('RangeIndex.copy', pdqh__twc,
        idx_cpy_arg_defaults, fn_str=fyrwk__jmtv, package_name='pandas',
        module_name='Index')
    if not is_overload_none(name):

        def impl(A, name=None, deep=False, dtype=None, names=None):
            return bodo.hiframes.pd_index_ext.init_range_index(A._start, A.
                _stop, A._step, name)
    else:

        def impl(A, name=None, deep=False, dtype=None, names=None):
            return bodo.hiframes.pd_index_ext.init_range_index(A._start, A.
                _stop, A._step, A._name)
    return impl


@box(RangeIndexType)
def box_range_index(typ, val, c):
    mxm__uztw = c.context.insert_const_string(c.builder.module, 'pandas')
    gmsz__moqir = c.pyapi.import_module_noblock(mxm__uztw)
    qxhq__xxut = cgutils.create_struct_proxy(typ)(c.context, c.builder, val)
    iesr__xycg = c.pyapi.from_native_value(types.int64, qxhq__xxut.start, c
        .env_manager)
    lok__vbgb = c.pyapi.from_native_value(types.int64, qxhq__xxut.stop, c.
        env_manager)
    hok__ybad = c.pyapi.from_native_value(types.int64, qxhq__xxut.step, c.
        env_manager)
    c.context.nrt.incref(c.builder, typ.name_typ, qxhq__xxut.name)
    fyqru__rsm = c.pyapi.from_native_value(typ.name_typ, qxhq__xxut.name, c
        .env_manager)
    args = c.pyapi.tuple_pack([iesr__xycg, lok__vbgb, hok__ybad])
    kws = c.pyapi.dict_pack([('name', fyqru__rsm)])
    txwyc__rhcf = c.pyapi.object_getattr_string(gmsz__moqir, 'RangeIndex')
    sigju__sgdcb = c.pyapi.call(txwyc__rhcf, args, kws)
    c.pyapi.decref(iesr__xycg)
    c.pyapi.decref(lok__vbgb)
    c.pyapi.decref(hok__ybad)
    c.pyapi.decref(fyqru__rsm)
    c.pyapi.decref(gmsz__moqir)
    c.pyapi.decref(txwyc__rhcf)
    c.pyapi.decref(args)
    c.pyapi.decref(kws)
    c.context.nrt.decref(c.builder, typ, val)
    return sigju__sgdcb


@intrinsic
def init_range_index(typingctx, start, stop, step, name=None):
    name = types.none if name is None else name
    empkm__fneqd = is_overload_constant_int(step) and get_overload_const_int(
        step) == 0

    def codegen(context, builder, signature, args):
        assert len(args) == 4
        if empkm__fneqd:
            raise_bodo_error('Step must not be zero')
        lqr__ofco = cgutils.is_scalar_zero(builder, args[2])
        rer__zcmqk = context.get_python_api(builder)
        with builder.if_then(lqr__ofco):
            rer__zcmqk.err_format('PyExc_ValueError', 'Step must not be zero')
            val = context.get_constant(types.int32, -1)
            builder.ret(val)
        qxhq__xxut = cgutils.create_struct_proxy(signature.return_type)(context
            , builder)
        qxhq__xxut.start = args[0]
        qxhq__xxut.stop = args[1]
        qxhq__xxut.step = args[2]
        qxhq__xxut.name = args[3]
        context.nrt.incref(builder, signature.return_type.name_typ, args[3])
        return qxhq__xxut._getvalue()
    return RangeIndexType(name)(start, stop, step, name), codegen


def init_range_index_equiv(self, scope, equiv_set, loc, args, kws):
    assert len(args) == 4 and not kws
    start, stop, step, elae__jvj = args
    if self.typemap[start.name] == types.IntegerLiteral(0) and self.typemap[
        step.name] == types.IntegerLiteral(1) and equiv_set.has_shape(stop):
        return ArrayAnalysis.AnalyzeResult(shape=stop, pre=[])
    return None


(ArrayAnalysis._analyze_op_call_bodo_hiframes_pd_index_ext_init_range_index
    ) = init_range_index_equiv


@unbox(RangeIndexType)
def unbox_range_index(typ, val, c):
    iesr__xycg = c.pyapi.object_getattr_string(val, 'start')
    start = c.pyapi.to_native_value(types.int64, iesr__xycg).value
    lok__vbgb = c.pyapi.object_getattr_string(val, 'stop')
    stop = c.pyapi.to_native_value(types.int64, lok__vbgb).value
    hok__ybad = c.pyapi.object_getattr_string(val, 'step')
    step = c.pyapi.to_native_value(types.int64, hok__ybad).value
    fyqru__rsm = c.pyapi.object_getattr_string(val, 'name')
    name = c.pyapi.to_native_value(typ.name_typ, fyqru__rsm).value
    c.pyapi.decref(iesr__xycg)
    c.pyapi.decref(lok__vbgb)
    c.pyapi.decref(hok__ybad)
    c.pyapi.decref(fyqru__rsm)
    qxhq__xxut = cgutils.create_struct_proxy(typ)(c.context, c.builder)
    qxhq__xxut.start = start
    qxhq__xxut.stop = stop
    qxhq__xxut.step = step
    qxhq__xxut.name = name
    return NativeValue(qxhq__xxut._getvalue())


@lower_constant(RangeIndexType)
def lower_constant_range_index(context, builder, ty, pyval):
    start = context.get_constant(types.int64, pyval.start)
    stop = context.get_constant(types.int64, pyval.stop)
    step = context.get_constant(types.int64, pyval.step)
    name = context.get_constant_generic(builder, ty.name_typ, pyval.name)
    return lir.Constant.literal_struct([start, stop, step, name])


@overload(pd.RangeIndex, no_unliteral=True, inline='always')
def range_index_overload(start=None, stop=None, step=None, dtype=None, copy
    =False, name=None):

    def _ensure_int_or_none(value, field):
        wgb__swngk = (
            'RangeIndex(...) must be called with integers, {value} was passed for {field}'
            )
        if not is_overload_none(value) and not isinstance(value, types.
            IntegerLiteral) and not isinstance(value, types.Integer):
            raise BodoError(wgb__swngk.format(value=value, field=field))
    _ensure_int_or_none(start, 'start')
    _ensure_int_or_none(stop, 'stop')
    _ensure_int_or_none(step, 'step')
    if is_overload_none(start) and is_overload_none(stop) and is_overload_none(
        step):
        wgb__swngk = 'RangeIndex(...) must be called with integers'
        raise BodoError(wgb__swngk)
    xstvy__qmjwz = 'start'
    jdoa__bhlli = 'stop'
    vwh__efm = 'step'
    if is_overload_none(start):
        xstvy__qmjwz = '0'
    if is_overload_none(stop):
        jdoa__bhlli = 'start'
        xstvy__qmjwz = '0'
    if is_overload_none(step):
        vwh__efm = '1'
    ncl__uyeu = """def _pd_range_index_imp(start=None, stop=None, step=None, dtype=None, copy=False, name=None):
"""
    ncl__uyeu += '  return init_range_index({}, {}, {}, name)\n'.format(
        xstvy__qmjwz, jdoa__bhlli, vwh__efm)
    iqmgk__pwkj = {}
    exec(ncl__uyeu, {'init_range_index': init_range_index}, iqmgk__pwkj)
    vtbq__cona = iqmgk__pwkj['_pd_range_index_imp']
    return vtbq__cona


@overload(pd.CategoricalIndex, no_unliteral=True, inline='always')
def categorical_index_overload(data=None, categories=None, ordered=None,
    dtype=None, copy=False, name=None):
    raise BodoError('pd.CategoricalIndex() initializer not yet supported.')


@overload_attribute(RangeIndexType, 'start')
def rangeIndex_get_start(ri):

    def impl(ri):
        return ri._start
    return impl


@overload_attribute(RangeIndexType, 'stop')
def rangeIndex_get_stop(ri):

    def impl(ri):
        return ri._stop
    return impl


@overload_attribute(RangeIndexType, 'step')
def rangeIndex_get_step(ri):

    def impl(ri):
        return ri._step
    return impl


@overload(operator.getitem, no_unliteral=True)
def overload_range_index_getitem(I, idx):
    if isinstance(I, RangeIndexType):
        if isinstance(types.unliteral(idx), types.Integer):
            return lambda I, idx: idx * I._step + I._start
        if isinstance(idx, types.SliceType):

            def impl(I, idx):
                xsryk__qsh = numba.cpython.unicode._normalize_slice(idx, len(I)
                    )
                name = bodo.hiframes.pd_index_ext.get_index_name(I)
                start = I._start + I._step * xsryk__qsh.start
                stop = I._start + I._step * xsryk__qsh.stop
                step = I._step * xsryk__qsh.step
                return bodo.hiframes.pd_index_ext.init_range_index(start,
                    stop, step, name)
            return impl
        return lambda I, idx: bodo.hiframes.pd_index_ext.init_numeric_index(np
            .arange(I._start, I._stop, I._step, np.int64)[idx], bodo.
            hiframes.pd_index_ext.get_index_name(I))


@overload(len, no_unliteral=True)
def overload_range_len(r):
    if isinstance(r, RangeIndexType):
        return lambda r: max(0, -(-(r._stop - r._start) // r._step))


class PeriodIndexType(types.IterableType, types.ArrayCompatible):

    def __init__(self, freq, name_typ=None):
        name_typ = types.none if name_typ is None else name_typ
        self.freq = freq
        self.name_typ = name_typ
        super(PeriodIndexType, self).__init__(name=
            'PeriodIndexType({}, {})'.format(freq, name_typ))
    ndim = 1

    @property
    def as_array(self):
        return types.Array(types.undefined, 1, 'C')

    def copy(self):
        return PeriodIndexType(self.freq, self.name_typ)

    @property
    def iterator_type(self):
        return bodo.utils.typing.BodoArrayIterator(self)

    @property
    def pandas_type_name(self):
        return 'object'

    @property
    def numpy_type_name(self):
        return f'period[{self.freq}]'


@typeof_impl.register(pd.PeriodIndex)
def typeof_pd_period_index(val, c):
    return PeriodIndexType(val.freqstr, get_val_type_maybe_str_literal(val.
        name))


@register_model(PeriodIndexType)
class PeriodIndexModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        deo__qhjso = [('data', bodo.IntegerArrayType(types.int64)), ('name',
            fe_type.name_typ), ('dict', types.DictType(types.int64, types.
            int64))]
        super(PeriodIndexModel, self).__init__(dmm, fe_type, deo__qhjso)


make_attribute_wrapper(PeriodIndexType, 'data', '_data')
make_attribute_wrapper(PeriodIndexType, 'name', '_name')
make_attribute_wrapper(PeriodIndexType, 'dict', '_dict')


@overload_method(PeriodIndexType, 'copy', no_unliteral=True)
def overload_period_index_copy(A, name=None, deep=False, dtype=None, names=None
    ):
    freq = A.freq
    pdqh__twc = dict(deep=deep, dtype=dtype, names=names)
    fyrwk__jmtv = idx_typ_to_format_str_map[PeriodIndexType].format('copy()')
    check_unsupported_args('PeriodIndex.copy', pdqh__twc,
        idx_cpy_arg_defaults, fn_str=fyrwk__jmtv, package_name='pandas',
        module_name='Index')
    if not is_overload_none(name):

        def impl(A, name=None, deep=False, dtype=None, names=None):
            return bodo.hiframes.pd_index_ext.init_period_index(A._data.
                copy(), name, freq)
    else:

        def impl(A, name=None, deep=False, dtype=None, names=None):
            return bodo.hiframes.pd_index_ext.init_period_index(A._data.
                copy(), A._name, freq)
    return impl


@intrinsic
def init_period_index(typingctx, data, name, freq):
    name = types.none if name is None else name

    def codegen(context, builder, signature, args):
        xeiw__gryez, nsgt__irg, elae__jvj = args
        byo__wvsup = signature.return_type
        ctcpn__xsfe = cgutils.create_struct_proxy(byo__wvsup)(context, builder)
        ctcpn__xsfe.data = xeiw__gryez
        ctcpn__xsfe.name = nsgt__irg
        context.nrt.incref(builder, signature.args[0], args[0])
        context.nrt.incref(builder, signature.args[1], args[1])
        ctcpn__xsfe.dict = context.compile_internal(builder, lambda : numba
            .typed.Dict.empty(types.int64, types.int64), types.DictType(
            types.int64, types.int64)(), [])
        return ctcpn__xsfe._getvalue()
    tnat__zxeq = get_overload_const_str(freq)
    oblu__azmv = PeriodIndexType(tnat__zxeq, name)
    sig = signature(oblu__azmv, data, name, freq)
    return sig, codegen


@box(PeriodIndexType)
def box_period_index(typ, val, c):
    mxm__uztw = c.context.insert_const_string(c.builder.module, 'pandas')
    gmsz__moqir = c.pyapi.import_module_noblock(mxm__uztw)
    waftq__ihx = cgutils.create_struct_proxy(typ)(c.context, c.builder, val)
    c.context.nrt.incref(c.builder, bodo.IntegerArrayType(types.int64),
        waftq__ihx.data)
    jgeh__lwf = c.pyapi.from_native_value(bodo.IntegerArrayType(types.int64
        ), waftq__ihx.data, c.env_manager)
    c.context.nrt.incref(c.builder, typ.name_typ, waftq__ihx.name)
    fyqru__rsm = c.pyapi.from_native_value(typ.name_typ, waftq__ihx.name, c
        .env_manager)
    wklfd__frfy = c.pyapi.string_from_constant_string(typ.freq)
    args = c.pyapi.tuple_pack([])
    kws = c.pyapi.dict_pack([('ordinal', jgeh__lwf), ('name', fyqru__rsm),
        ('freq', wklfd__frfy)])
    txwyc__rhcf = c.pyapi.object_getattr_string(gmsz__moqir, 'PeriodIndex')
    sigju__sgdcb = c.pyapi.call(txwyc__rhcf, args, kws)
    c.pyapi.decref(jgeh__lwf)
    c.pyapi.decref(fyqru__rsm)
    c.pyapi.decref(wklfd__frfy)
    c.pyapi.decref(gmsz__moqir)
    c.pyapi.decref(txwyc__rhcf)
    c.pyapi.decref(args)
    c.pyapi.decref(kws)
    c.context.nrt.decref(c.builder, typ, val)
    return sigju__sgdcb


@unbox(PeriodIndexType)
def unbox_period_index(typ, val, c):
    arr_typ = bodo.IntegerArrayType(types.int64)
    sciv__wblc = c.pyapi.object_getattr_string(val, 'asi8')
    ylsqg__ddxfi = c.pyapi.call_method(val, 'isna', ())
    fyqru__rsm = c.pyapi.object_getattr_string(val, 'name')
    name = c.pyapi.to_native_value(typ.name_typ, fyqru__rsm).value
    mxm__uztw = c.context.insert_const_string(c.builder.module, 'pandas')
    hdp__eos = c.pyapi.import_module_noblock(mxm__uztw)
    minzv__chans = c.pyapi.object_getattr_string(hdp__eos, 'arrays')
    jgeh__lwf = c.pyapi.call_method(minzv__chans, 'IntegerArray', (
        sciv__wblc, ylsqg__ddxfi))
    data = c.pyapi.to_native_value(arr_typ, jgeh__lwf).value
    c.pyapi.decref(sciv__wblc)
    c.pyapi.decref(ylsqg__ddxfi)
    c.pyapi.decref(fyqru__rsm)
    c.pyapi.decref(hdp__eos)
    c.pyapi.decref(minzv__chans)
    c.pyapi.decref(jgeh__lwf)
    waftq__ihx = cgutils.create_struct_proxy(typ)(c.context, c.builder)
    waftq__ihx.data = data
    waftq__ihx.name = name
    awq__dix, urpk__nfmm = c.pyapi.call_jit_code(lambda : numba.typed.Dict.
        empty(types.int64, types.int64), types.DictType(types.int64, types.
        int64)(), [])
    waftq__ihx.dict = urpk__nfmm
    return NativeValue(waftq__ihx._getvalue())


class CategoricalIndexType(types.IterableType, types.ArrayCompatible):

    def __init__(self, data, name_typ=None):
        from bodo.hiframes.pd_categorical_ext import CategoricalArrayType
        assert isinstance(data, CategoricalArrayType
            ), 'CategoricalIndexType expects CategoricalArrayType'
        name_typ = types.none if name_typ is None else name_typ
        self.name_typ = name_typ
        self.data = data
        super(CategoricalIndexType, self).__init__(name=
            f'CategoricalIndexType(data={self.data}, name={name_typ})')
    ndim = 1

    def copy(self):
        return CategoricalIndexType(self.data, self.name_typ)

    @property
    def as_array(self):
        return types.Array(types.undefined, 1, 'C')

    @property
    def dtype(self):
        return self.data.dtype

    @property
    def key(self):
        return self.data, self.name_typ

    @property
    def mangling_args(self):
        return self.__class__.__name__, (self._code,)

    @property
    def pandas_type_name(self):
        return 'categorical'

    @property
    def numpy_type_name(self):
        from bodo.hiframes.pd_categorical_ext import get_categories_int_type
        return str(get_categories_int_type(self.dtype))

    @property
    def iterator_type(self):
        return bodo.utils.typing.BodoArrayIterator(self, self.dtype.elem_type)


@register_model(CategoricalIndexType)
class CategoricalIndexTypeModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        from bodo.hiframes.pd_categorical_ext import get_categories_int_type
        mba__oni = get_categories_int_type(fe_type.data.dtype)
        deo__qhjso = [('data', fe_type.data), ('name', fe_type.name_typ), (
            'dict', types.DictType(mba__oni, types.int64))]
        super(CategoricalIndexTypeModel, self).__init__(dmm, fe_type,
            deo__qhjso)


@typeof_impl.register(pd.CategoricalIndex)
def typeof_categorical_index(val, c):
    return CategoricalIndexType(bodo.typeof(val.values),
        get_val_type_maybe_str_literal(val.name))


@box(CategoricalIndexType)
def box_categorical_index(typ, val, c):
    mxm__uztw = c.context.insert_const_string(c.builder.module, 'pandas')
    hdp__eos = c.pyapi.import_module_noblock(mxm__uztw)
    iolfz__lhgf = numba.core.cgutils.create_struct_proxy(typ)(c.context, c.
        builder, val)
    c.context.nrt.incref(c.builder, typ.data, iolfz__lhgf.data)
    uxp__qpe = c.pyapi.from_native_value(typ.data, iolfz__lhgf.data, c.
        env_manager)
    c.context.nrt.incref(c.builder, typ.name_typ, iolfz__lhgf.name)
    fyqru__rsm = c.pyapi.from_native_value(typ.name_typ, iolfz__lhgf.name,
        c.env_manager)
    args = c.pyapi.tuple_pack([uxp__qpe])
    kws = c.pyapi.dict_pack([('name', fyqru__rsm)])
    txwyc__rhcf = c.pyapi.object_getattr_string(hdp__eos, 'CategoricalIndex')
    plegg__ikob = c.pyapi.call(txwyc__rhcf, args, kws)
    c.pyapi.decref(uxp__qpe)
    c.pyapi.decref(fyqru__rsm)
    c.pyapi.decref(hdp__eos)
    c.pyapi.decref(txwyc__rhcf)
    c.pyapi.decref(args)
    c.pyapi.decref(kws)
    c.context.nrt.decref(c.builder, typ, val)
    return plegg__ikob


@unbox(CategoricalIndexType)
def unbox_categorical_index(typ, val, c):
    from bodo.hiframes.pd_categorical_ext import get_categories_int_type
    rhovc__ampy = c.pyapi.object_getattr_string(val, 'values')
    data = c.pyapi.to_native_value(typ.data, rhovc__ampy).value
    fyqru__rsm = c.pyapi.object_getattr_string(val, 'name')
    name = c.pyapi.to_native_value(typ.name_typ, fyqru__rsm).value
    c.pyapi.decref(rhovc__ampy)
    c.pyapi.decref(fyqru__rsm)
    waftq__ihx = cgutils.create_struct_proxy(typ)(c.context, c.builder)
    waftq__ihx.data = data
    waftq__ihx.name = name
    dtype = get_categories_int_type(typ.data.dtype)
    awq__dix, urpk__nfmm = c.pyapi.call_jit_code(lambda : numba.typed.Dict.
        empty(dtype, types.int64), types.DictType(dtype, types.int64)(), [])
    waftq__ihx.dict = urpk__nfmm
    return NativeValue(waftq__ihx._getvalue())


@intrinsic
def init_categorical_index(typingctx, data, name=None):
    name = types.none if name is None else name

    def codegen(context, builder, signature, args):
        from bodo.hiframes.pd_categorical_ext import get_categories_int_type
        xeiw__gryez, nsgt__irg = args
        iolfz__lhgf = cgutils.create_struct_proxy(signature.return_type)(
            context, builder)
        iolfz__lhgf.data = xeiw__gryez
        iolfz__lhgf.name = nsgt__irg
        context.nrt.incref(builder, signature.args[0], xeiw__gryez)
        context.nrt.incref(builder, signature.args[1], nsgt__irg)
        dtype = get_categories_int_type(signature.return_type.data.dtype)
        iolfz__lhgf.dict = context.compile_internal(builder, lambda : numba
            .typed.Dict.empty(dtype, types.int64), types.DictType(dtype,
            types.int64)(), [])
        return iolfz__lhgf._getvalue()
    oblu__azmv = CategoricalIndexType(data, name)
    sig = signature(oblu__azmv, data, name)
    return sig, codegen


(ArrayAnalysis.
    _analyze_op_call_bodo_hiframes_pd_index_ext_init_categorical_index
    ) = init_index_equiv
make_attribute_wrapper(CategoricalIndexType, 'data', '_data')
make_attribute_wrapper(CategoricalIndexType, 'name', '_name')
make_attribute_wrapper(CategoricalIndexType, 'dict', '_dict')


@overload_method(CategoricalIndexType, 'copy', no_unliteral=True)
def overload_categorical_index_copy(A, name=None, deep=False, dtype=None,
    names=None):
    fyrwk__jmtv = idx_typ_to_format_str_map[CategoricalIndexType].format(
        'copy()')
    pdqh__twc = dict(deep=deep, dtype=dtype, names=names)
    check_unsupported_args('CategoricalIndex.copy', pdqh__twc,
        idx_cpy_arg_defaults, fn_str=fyrwk__jmtv, package_name='pandas',
        module_name='Index')
    if not is_overload_none(name):

        def impl(A, name=None, deep=False, dtype=None, names=None):
            return bodo.hiframes.pd_index_ext.init_categorical_index(A.
                _data.copy(), name)
    else:

        def impl(A, name=None, deep=False, dtype=None, names=None):
            return bodo.hiframes.pd_index_ext.init_categorical_index(A.
                _data.copy(), A._name)
    return impl


class IntervalIndexType(types.ArrayCompatible):

    def __init__(self, data, name_typ=None):
        from bodo.libs.interval_arr_ext import IntervalArrayType
        assert isinstance(data, IntervalArrayType
            ), 'IntervalIndexType expects IntervalArrayType'
        name_typ = types.none if name_typ is None else name_typ
        self.name_typ = name_typ
        self.data = data
        super(IntervalIndexType, self).__init__(name=
            f'IntervalIndexType(data={self.data}, name={name_typ})')
    ndim = 1

    def copy(self):
        return IntervalIndexType(self.data, self.name_typ)

    @property
    def as_array(self):
        return types.Array(types.undefined, 1, 'C')

    @property
    def key(self):
        return self.data, self.name_typ

    @property
    def mangling_args(self):
        return self.__class__.__name__, (self._code,)

    @property
    def pandas_type_name(self):
        return 'object'

    @property
    def numpy_type_name(self):
        return f'interval[{self.data.arr_type.dtype}, right]'


@register_model(IntervalIndexType)
class IntervalIndexTypeModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        deo__qhjso = [('data', fe_type.data), ('name', fe_type.name_typ), (
            'dict', types.DictType(types.UniTuple(fe_type.data.arr_type.
            dtype, 2), types.int64))]
        super(IntervalIndexTypeModel, self).__init__(dmm, fe_type, deo__qhjso)


@typeof_impl.register(pd.IntervalIndex)
def typeof_interval_index(val, c):
    return IntervalIndexType(bodo.typeof(val.values),
        get_val_type_maybe_str_literal(val.name))


@box(IntervalIndexType)
def box_interval_index(typ, val, c):
    mxm__uztw = c.context.insert_const_string(c.builder.module, 'pandas')
    hdp__eos = c.pyapi.import_module_noblock(mxm__uztw)
    qdw__zlsqp = numba.core.cgutils.create_struct_proxy(typ)(c.context, c.
        builder, val)
    c.context.nrt.incref(c.builder, typ.data, qdw__zlsqp.data)
    uxp__qpe = c.pyapi.from_native_value(typ.data, qdw__zlsqp.data, c.
        env_manager)
    c.context.nrt.incref(c.builder, typ.name_typ, qdw__zlsqp.name)
    fyqru__rsm = c.pyapi.from_native_value(typ.name_typ, qdw__zlsqp.name, c
        .env_manager)
    args = c.pyapi.tuple_pack([uxp__qpe])
    kws = c.pyapi.dict_pack([('name', fyqru__rsm)])
    txwyc__rhcf = c.pyapi.object_getattr_string(hdp__eos, 'IntervalIndex')
    plegg__ikob = c.pyapi.call(txwyc__rhcf, args, kws)
    c.pyapi.decref(uxp__qpe)
    c.pyapi.decref(fyqru__rsm)
    c.pyapi.decref(hdp__eos)
    c.pyapi.decref(txwyc__rhcf)
    c.pyapi.decref(args)
    c.pyapi.decref(kws)
    c.context.nrt.decref(c.builder, typ, val)
    return plegg__ikob


@unbox(IntervalIndexType)
def unbox_interval_index(typ, val, c):
    rhovc__ampy = c.pyapi.object_getattr_string(val, 'values')
    data = c.pyapi.to_native_value(typ.data, rhovc__ampy).value
    fyqru__rsm = c.pyapi.object_getattr_string(val, 'name')
    name = c.pyapi.to_native_value(typ.name_typ, fyqru__rsm).value
    c.pyapi.decref(rhovc__ampy)
    c.pyapi.decref(fyqru__rsm)
    waftq__ihx = cgutils.create_struct_proxy(typ)(c.context, c.builder)
    waftq__ihx.data = data
    waftq__ihx.name = name
    dtype = types.UniTuple(typ.data.arr_type.dtype, 2)
    awq__dix, urpk__nfmm = c.pyapi.call_jit_code(lambda : numba.typed.Dict.
        empty(dtype, types.int64), types.DictType(dtype, types.int64)(), [])
    waftq__ihx.dict = urpk__nfmm
    return NativeValue(waftq__ihx._getvalue())


@intrinsic
def init_interval_index(typingctx, data, name=None):
    name = types.none if name is None else name

    def codegen(context, builder, signature, args):
        xeiw__gryez, nsgt__irg = args
        qdw__zlsqp = cgutils.create_struct_proxy(signature.return_type)(context
            , builder)
        qdw__zlsqp.data = xeiw__gryez
        qdw__zlsqp.name = nsgt__irg
        context.nrt.incref(builder, signature.args[0], xeiw__gryez)
        context.nrt.incref(builder, signature.args[1], nsgt__irg)
        dtype = types.UniTuple(data.arr_type.dtype, 2)
        qdw__zlsqp.dict = context.compile_internal(builder, lambda : numba.
            typed.Dict.empty(dtype, types.int64), types.DictType(dtype,
            types.int64)(), [])
        return qdw__zlsqp._getvalue()
    oblu__azmv = IntervalIndexType(data, name)
    sig = signature(oblu__azmv, data, name)
    return sig, codegen


(ArrayAnalysis._analyze_op_call_bodo_hiframes_pd_index_ext_init_interval_index
    ) = init_index_equiv
make_attribute_wrapper(IntervalIndexType, 'data', '_data')
make_attribute_wrapper(IntervalIndexType, 'name', '_name')
make_attribute_wrapper(IntervalIndexType, 'dict', '_dict')


class NumericIndexType(types.IterableType, types.ArrayCompatible):

    def __init__(self, dtype, name_typ=None, data=None):
        name_typ = types.none if name_typ is None else name_typ
        self.dtype = dtype
        self.name_typ = name_typ
        data = dtype_to_array_type(dtype) if data is None else data
        self.data = data
        super(NumericIndexType, self).__init__(name=
            f'NumericIndexType({dtype}, {name_typ}, {data})')
    ndim = 1

    @property
    def as_array(self):
        return types.Array(types.undefined, 1, 'C')

    def copy(self):
        return NumericIndexType(self.dtype, self.name_typ, self.data)

    @property
    def iterator_type(self):
        return bodo.utils.typing.BodoArrayIterator(self)

    @property
    def pandas_type_name(self):
        return str(self.dtype)

    @property
    def numpy_type_name(self):
        return str(self.dtype)


with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    Int64Index = pd.Int64Index
    UInt64Index = pd.UInt64Index
    Float64Index = pd.Float64Index


@typeof_impl.register(Int64Index)
def typeof_pd_int64_index(val, c):
    return NumericIndexType(types.int64, get_val_type_maybe_str_literal(val
        .name))


@typeof_impl.register(UInt64Index)
def typeof_pd_uint64_index(val, c):
    return NumericIndexType(types.uint64, get_val_type_maybe_str_literal(
        val.name))


@typeof_impl.register(Float64Index)
def typeof_pd_float64_index(val, c):
    return NumericIndexType(types.float64, get_val_type_maybe_str_literal(
        val.name))


@register_model(NumericIndexType)
class NumericIndexModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        deo__qhjso = [('data', fe_type.data), ('name', fe_type.name_typ), (
            'dict', types.DictType(fe_type.dtype, types.int64))]
        super(NumericIndexModel, self).__init__(dmm, fe_type, deo__qhjso)


make_attribute_wrapper(NumericIndexType, 'data', '_data')
make_attribute_wrapper(NumericIndexType, 'name', '_name')
make_attribute_wrapper(NumericIndexType, 'dict', '_dict')


@overload_method(NumericIndexType, 'copy', no_unliteral=True)
def overload_numeric_index_copy(A, name=None, deep=False, dtype=None, names
    =None):
    fyrwk__jmtv = idx_typ_to_format_str_map[NumericIndexType].format('copy()')
    pdqh__twc = dict(deep=deep, dtype=dtype, names=names)
    check_unsupported_args('Index.copy', pdqh__twc, idx_cpy_arg_defaults,
        fn_str=fyrwk__jmtv, package_name='pandas', module_name='Index')
    if not is_overload_none(name):

        def impl(A, name=None, deep=False, dtype=None, names=None):
            return bodo.hiframes.pd_index_ext.init_numeric_index(A._data.
                copy(), name)
    else:

        def impl(A, name=None, deep=False, dtype=None, names=None):
            return bodo.hiframes.pd_index_ext.init_numeric_index(A._data.
                copy(), A._name)
    return impl


@box(NumericIndexType)
def box_numeric_index(typ, val, c):
    mxm__uztw = c.context.insert_const_string(c.builder.module, 'pandas')
    gmsz__moqir = c.pyapi.import_module_noblock(mxm__uztw)
    waftq__ihx = cgutils.create_struct_proxy(typ)(c.context, c.builder, val)
    c.context.nrt.incref(c.builder, typ.data, waftq__ihx.data)
    jgeh__lwf = c.pyapi.from_native_value(typ.data, waftq__ihx.data, c.
        env_manager)
    c.context.nrt.incref(c.builder, typ.name_typ, waftq__ihx.name)
    fyqru__rsm = c.pyapi.from_native_value(typ.name_typ, waftq__ihx.name, c
        .env_manager)
    eipq__lrrkt = c.pyapi.make_none()
    dgief__tzzy = c.pyapi.bool_from_bool(c.context.get_constant(types.bool_,
        False))
    sigju__sgdcb = c.pyapi.call_method(gmsz__moqir, 'Index', (jgeh__lwf,
        eipq__lrrkt, dgief__tzzy, fyqru__rsm))
    c.pyapi.decref(jgeh__lwf)
    c.pyapi.decref(eipq__lrrkt)
    c.pyapi.decref(dgief__tzzy)
    c.pyapi.decref(fyqru__rsm)
    c.pyapi.decref(gmsz__moqir)
    c.context.nrt.decref(c.builder, typ, val)
    return sigju__sgdcb


@intrinsic
def init_numeric_index(typingctx, data, name=None):
    name = types.none if is_overload_none(name) else name

    def codegen(context, builder, signature, args):
        assert len(args) == 2
        byo__wvsup = signature.return_type
        waftq__ihx = cgutils.create_struct_proxy(byo__wvsup)(context, builder)
        waftq__ihx.data = args[0]
        waftq__ihx.name = args[1]
        context.nrt.incref(builder, byo__wvsup.data, args[0])
        context.nrt.incref(builder, byo__wvsup.name_typ, args[1])
        dtype = byo__wvsup.dtype
        waftq__ihx.dict = context.compile_internal(builder, lambda : numba.
            typed.Dict.empty(dtype, types.int64), types.DictType(dtype,
            types.int64)(), [])
        return waftq__ihx._getvalue()
    return NumericIndexType(data.dtype, name, data)(data, name), codegen


(ArrayAnalysis._analyze_op_call_bodo_hiframes_pd_index_ext_init_numeric_index
    ) = init_index_equiv


@unbox(NumericIndexType)
def unbox_numeric_index(typ, val, c):
    rhovc__ampy = c.pyapi.object_getattr_string(val, 'values')
    data = c.pyapi.to_native_value(typ.data, rhovc__ampy).value
    fyqru__rsm = c.pyapi.object_getattr_string(val, 'name')
    name = c.pyapi.to_native_value(typ.name_typ, fyqru__rsm).value
    c.pyapi.decref(rhovc__ampy)
    c.pyapi.decref(fyqru__rsm)
    waftq__ihx = cgutils.create_struct_proxy(typ)(c.context, c.builder)
    waftq__ihx.data = data
    waftq__ihx.name = name
    dtype = typ.dtype
    awq__dix, urpk__nfmm = c.pyapi.call_jit_code(lambda : numba.typed.Dict.
        empty(dtype, types.int64), types.DictType(dtype, types.int64)(), [])
    waftq__ihx.dict = urpk__nfmm
    return NativeValue(waftq__ihx._getvalue())


def create_numeric_constructor(func, func_str, default_dtype):

    def overload_impl(data=None, dtype=None, copy=False, name=None):
        oqnjc__njy = dict(dtype=dtype)
        zcymq__nle = dict(dtype=None)
        check_unsupported_args(func_str, oqnjc__njy, zcymq__nle,
            package_name='pandas', module_name='Index')
        if is_overload_false(copy):

            def impl(data=None, dtype=None, copy=False, name=None):
                tif__bqq = bodo.utils.conversion.coerce_to_ndarray(data)
                qok__vyk = bodo.utils.conversion.fix_arr_dtype(tif__bqq, np
                    .dtype(default_dtype))
                return bodo.hiframes.pd_index_ext.init_numeric_index(qok__vyk,
                    name)
        else:

            def impl(data=None, dtype=None, copy=False, name=None):
                tif__bqq = bodo.utils.conversion.coerce_to_ndarray(data)
                if copy:
                    tif__bqq = tif__bqq.copy()
                qok__vyk = bodo.utils.conversion.fix_arr_dtype(tif__bqq, np
                    .dtype(default_dtype))
                return bodo.hiframes.pd_index_ext.init_numeric_index(qok__vyk,
                    name)
        return impl
    return overload_impl


def _install_numeric_constructors():
    for func, func_str, default_dtype in ((Int64Index, 'pandas.Int64Index',
        np.int64), (UInt64Index, 'pandas.UInt64Index', np.uint64), (
        Float64Index, 'pandas.Float64Index', np.float64)):
        overload_impl = create_numeric_constructor(func, func_str,
            default_dtype)
        overload(func, no_unliteral=True)(overload_impl)


_install_numeric_constructors()


class StringIndexType(types.IterableType, types.ArrayCompatible):

    def __init__(self, name_typ=None, data_typ=None):
        name_typ = types.none if name_typ is None else name_typ
        self.name_typ = name_typ
        self.data = string_array_type if data_typ is None else data_typ
        super(StringIndexType, self).__init__(name=
            f'StringIndexType({name_typ}, {self.data})')
    ndim = 1

    @property
    def as_array(self):
        return types.Array(types.undefined, 1, 'C')

    def copy(self):
        return StringIndexType(self.name_typ, self.data)

    @property
    def dtype(self):
        return string_type

    @property
    def pandas_type_name(self):
        return 'unicode'

    @property
    def numpy_type_name(self):
        return 'object'

    @property
    def iterator_type(self):
        return bodo.utils.typing.BodoArrayIterator(self)


@register_model(StringIndexType)
class StringIndexModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        deo__qhjso = [('data', fe_type.data), ('name', fe_type.name_typ), (
            'dict', types.DictType(string_type, types.int64))]
        super(StringIndexModel, self).__init__(dmm, fe_type, deo__qhjso)


make_attribute_wrapper(StringIndexType, 'data', '_data')
make_attribute_wrapper(StringIndexType, 'name', '_name')
make_attribute_wrapper(StringIndexType, 'dict', '_dict')


class BinaryIndexType(types.IterableType, types.ArrayCompatible):

    def __init__(self, name_typ=None, data_typ=None):
        assert data_typ is None or data_typ == binary_array_type, 'data_typ must be binary_array_type'
        name_typ = types.none if name_typ is None else name_typ
        self.name_typ = name_typ
        self.data = binary_array_type
        super(BinaryIndexType, self).__init__(name='BinaryIndexType({})'.
            format(name_typ))
    ndim = 1

    @property
    def as_array(self):
        return types.Array(types.undefined, 1, 'C')

    def copy(self):
        return BinaryIndexType(self.name_typ)

    @property
    def dtype(self):
        return bytes_type

    @property
    def pandas_type_name(self):
        return 'bytes'

    @property
    def numpy_type_name(self):
        return 'object'

    @property
    def iterator_type(self):
        return bodo.utils.typing.BodoArrayIterator(self)


@register_model(BinaryIndexType)
class BinaryIndexModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        deo__qhjso = [('data', binary_array_type), ('name', fe_type.
            name_typ), ('dict', types.DictType(bytes_type, types.int64))]
        super(BinaryIndexModel, self).__init__(dmm, fe_type, deo__qhjso)


make_attribute_wrapper(BinaryIndexType, 'data', '_data')
make_attribute_wrapper(BinaryIndexType, 'name', '_name')
make_attribute_wrapper(BinaryIndexType, 'dict', '_dict')


@unbox(BinaryIndexType)
@unbox(StringIndexType)
def unbox_binary_str_index(typ, val, c):
    gps__gxxcf = typ.data
    scalar_type = typ.data.dtype
    rhovc__ampy = c.pyapi.object_getattr_string(val, 'values')
    data = c.pyapi.to_native_value(gps__gxxcf, rhovc__ampy).value
    fyqru__rsm = c.pyapi.object_getattr_string(val, 'name')
    name = c.pyapi.to_native_value(typ.name_typ, fyqru__rsm).value
    c.pyapi.decref(rhovc__ampy)
    c.pyapi.decref(fyqru__rsm)
    waftq__ihx = cgutils.create_struct_proxy(typ)(c.context, c.builder)
    waftq__ihx.data = data
    waftq__ihx.name = name
    awq__dix, urpk__nfmm = c.pyapi.call_jit_code(lambda : numba.typed.Dict.
        empty(scalar_type, types.int64), types.DictType(scalar_type, types.
        int64)(), [])
    waftq__ihx.dict = urpk__nfmm
    return NativeValue(waftq__ihx._getvalue())


@box(BinaryIndexType)
@box(StringIndexType)
def box_binary_str_index(typ, val, c):
    gps__gxxcf = typ.data
    mxm__uztw = c.context.insert_const_string(c.builder.module, 'pandas')
    gmsz__moqir = c.pyapi.import_module_noblock(mxm__uztw)
    waftq__ihx = cgutils.create_struct_proxy(typ)(c.context, c.builder, val)
    c.context.nrt.incref(c.builder, gps__gxxcf, waftq__ihx.data)
    jgeh__lwf = c.pyapi.from_native_value(gps__gxxcf, waftq__ihx.data, c.
        env_manager)
    c.context.nrt.incref(c.builder, typ.name_typ, waftq__ihx.name)
    fyqru__rsm = c.pyapi.from_native_value(typ.name_typ, waftq__ihx.name, c
        .env_manager)
    eipq__lrrkt = c.pyapi.make_none()
    dgief__tzzy = c.pyapi.bool_from_bool(c.context.get_constant(types.bool_,
        False))
    sigju__sgdcb = c.pyapi.call_method(gmsz__moqir, 'Index', (jgeh__lwf,
        eipq__lrrkt, dgief__tzzy, fyqru__rsm))
    c.pyapi.decref(jgeh__lwf)
    c.pyapi.decref(eipq__lrrkt)
    c.pyapi.decref(dgief__tzzy)
    c.pyapi.decref(fyqru__rsm)
    c.pyapi.decref(gmsz__moqir)
    c.context.nrt.decref(c.builder, typ, val)
    return sigju__sgdcb


@intrinsic
def init_binary_str_index(typingctx, data, name=None):
    name = types.none if name is None else name
    sig = type(bodo.utils.typing.get_index_type_from_dtype(data.dtype))(name,
        data)(data, name)
    ijrp__tqm = get_binary_str_codegen(is_binary=data.dtype == bytes_type)
    return sig, ijrp__tqm


(ArrayAnalysis.
    _analyze_op_call_bodo_hiframes_pd_index_ext_init_binary_str_index
    ) = init_index_equiv


def get_binary_str_codegen(is_binary=False):
    if is_binary:
        qhsby__xfvv = 'bytes_type'
    else:
        qhsby__xfvv = 'string_type'
    ncl__uyeu = 'def impl(context, builder, signature, args):\n'
    ncl__uyeu += '    assert len(args) == 2\n'
    ncl__uyeu += '    index_typ = signature.return_type\n'
    ncl__uyeu += (
        '    index_val = cgutils.create_struct_proxy(index_typ)(context, builder)\n'
        )
    ncl__uyeu += '    index_val.data = args[0]\n'
    ncl__uyeu += '    index_val.name = args[1]\n'
    ncl__uyeu += '    # increase refcount of stored values\n'
    ncl__uyeu += (
        '    context.nrt.incref(builder, signature.args[0], args[0])\n')
    ncl__uyeu += (
        '    context.nrt.incref(builder, index_typ.name_typ, args[1])\n')
    ncl__uyeu += '    # create empty dict for get_loc hashmap\n'
    ncl__uyeu += '    index_val.dict = context.compile_internal(\n'
    ncl__uyeu += '       builder,\n'
    ncl__uyeu += (
        f'       lambda: numba.typed.Dict.empty({qhsby__xfvv}, types.int64),\n'
        )
    ncl__uyeu += (
        f'        types.DictType({qhsby__xfvv}, types.int64)(), [],)\n')
    ncl__uyeu += '    return index_val._getvalue()\n'
    iqmgk__pwkj = {}
    exec(ncl__uyeu, {'bodo': bodo, 'signature': signature, 'cgutils':
        cgutils, 'numba': numba, 'types': types, 'bytes_type': bytes_type,
        'string_type': string_type}, iqmgk__pwkj)
    impl = iqmgk__pwkj['impl']
    return impl


@overload_method(BinaryIndexType, 'copy', no_unliteral=True)
@overload_method(StringIndexType, 'copy', no_unliteral=True)
def overload_binary_string_index_copy(A, name=None, deep=False, dtype=None,
    names=None):
    typ = type(A)
    fyrwk__jmtv = idx_typ_to_format_str_map[typ].format('copy()')
    pdqh__twc = dict(deep=deep, dtype=dtype, names=names)
    check_unsupported_args('Index.copy', pdqh__twc, idx_cpy_arg_defaults,
        fn_str=fyrwk__jmtv, package_name='pandas', module_name='Index')
    if not is_overload_none(name):

        def impl(A, name=None, deep=False, dtype=None, names=None):
            return bodo.hiframes.pd_index_ext.init_binary_str_index(A._data
                .copy(), name)
    else:

        def impl(A, name=None, deep=False, dtype=None, names=None):
            return bodo.hiframes.pd_index_ext.init_binary_str_index(A._data
                .copy(), A._name)
    return impl


@overload_attribute(BinaryIndexType, 'name')
@overload_attribute(StringIndexType, 'name')
@overload_attribute(DatetimeIndexType, 'name')
@overload_attribute(TimedeltaIndexType, 'name')
@overload_attribute(RangeIndexType, 'name')
@overload_attribute(PeriodIndexType, 'name')
@overload_attribute(NumericIndexType, 'name')
@overload_attribute(IntervalIndexType, 'name')
@overload_attribute(CategoricalIndexType, 'name')
@overload_attribute(MultiIndexType, 'name')
def Index_get_name(i):

    def impl(i):
        return i._name
    return impl


@overload(operator.getitem, no_unliteral=True)
def overload_index_getitem(I, ind):
    if isinstance(I, (NumericIndexType, StringIndexType, BinaryIndexType)
        ) and isinstance(ind, types.Integer):
        return lambda I, ind: bodo.hiframes.pd_index_ext.get_index_data(I)[ind]
    if isinstance(I, NumericIndexType):
        return lambda I, ind: bodo.hiframes.pd_index_ext.init_numeric_index(
            bodo.hiframes.pd_index_ext.get_index_data(I)[ind], bodo.
            hiframes.pd_index_ext.get_index_name(I))
    if isinstance(I, (StringIndexType, BinaryIndexType)):
        return lambda I, ind: bodo.hiframes.pd_index_ext.init_binary_str_index(
            bodo.hiframes.pd_index_ext.get_index_data(I)[ind], bodo.
            hiframes.pd_index_ext.get_index_name(I))


def array_type_to_index(arr_typ, name_typ=None):
    if is_str_arr_type(arr_typ):
        return StringIndexType(name_typ, arr_typ)
    if arr_typ == bodo.binary_array_type:
        return BinaryIndexType(name_typ)
    assert isinstance(arr_typ, (types.Array, IntegerArrayType, bodo.
        CategoricalArrayType)) or arr_typ in (bodo.datetime_date_array_type,
        bodo.boolean_array
        ), f'Converting array type {arr_typ} to index not supported'
    if (arr_typ == bodo.datetime_date_array_type or arr_typ.dtype == types.
        NPDatetime('ns')):
        return DatetimeIndexType(name_typ)
    if isinstance(arr_typ, bodo.DatetimeArrayType):
        return DatetimeIndexType(name_typ, arr_typ)
    if isinstance(arr_typ, bodo.CategoricalArrayType):
        return CategoricalIndexType(arr_typ, name_typ)
    if arr_typ.dtype == types.NPTimedelta('ns'):
        return TimedeltaIndexType(name_typ)
    if isinstance(arr_typ.dtype, (types.Integer, types.Float, types.Boolean)):
        return NumericIndexType(arr_typ.dtype, name_typ, arr_typ)
    raise BodoError(f'invalid index type {arr_typ}')


def is_pd_index_type(t):
    return isinstance(t, (NumericIndexType, DatetimeIndexType,
        TimedeltaIndexType, IntervalIndexType, CategoricalIndexType,
        PeriodIndexType, StringIndexType, BinaryIndexType, RangeIndexType,
        HeterogeneousIndexType))


def _verify_setop_compatible(func_name, I, other):
    if not is_pd_index_type(other) and not isinstance(other, (SeriesType,
        types.Array)):
        raise BodoError(
            f'pd.Index.{func_name}(): unsupported type for argument other: {other}'
            )
    hkzju__zgu = I.dtype if not isinstance(I, RangeIndexType) else types.int64
    yzkcb__csa = other.dtype if not isinstance(other, RangeIndexType
        ) else types.int64
    if hkzju__zgu != yzkcb__csa:
        raise BodoError(
            f'Index.{func_name}(): incompatible types {hkzju__zgu} and {yzkcb__csa}'
            )


@overload_method(NumericIndexType, 'union', inline='always')
@overload_method(StringIndexType, 'union', inline='always')
@overload_method(BinaryIndexType, 'union', inline='always')
@overload_method(DatetimeIndexType, 'union', inline='always')
@overload_method(TimedeltaIndexType, 'union', inline='always')
@overload_method(RangeIndexType, 'union', inline='always')
def overload_index_union(I, other, sort=None):
    grdlp__pza = dict(sort=sort)
    qvhp__whkh = dict(sort=None)
    check_unsupported_args('Index.union', grdlp__pza, qvhp__whkh,
        package_name='pandas', module_name='Index')
    _verify_setop_compatible('union', I, other)
    bds__hywti = get_index_constructor(I) if not isinstance(I, RangeIndexType
        ) else init_numeric_index

    def impl(I, other, sort=None):
        jdsv__rdb = bodo.utils.conversion.coerce_to_array(I)
        zar__tfy = bodo.utils.conversion.coerce_to_array(other)
        gyzvi__vti = bodo.libs.array_kernels.concat([jdsv__rdb, zar__tfy])
        ejt__tnyp = bodo.libs.array_kernels.unique(gyzvi__vti)
        return bds__hywti(ejt__tnyp, None)
    return impl


@overload_method(NumericIndexType, 'intersection', inline='always')
@overload_method(StringIndexType, 'intersection', inline='always')
@overload_method(BinaryIndexType, 'intersection', inline='always')
@overload_method(DatetimeIndexType, 'intersection', inline='always')
@overload_method(TimedeltaIndexType, 'intersection', inline='always')
@overload_method(RangeIndexType, 'intersection', inline='always')
def overload_index_intersection(I, other, sort=None):
    grdlp__pza = dict(sort=sort)
    qvhp__whkh = dict(sort=None)
    check_unsupported_args('Index.intersection', grdlp__pza, qvhp__whkh,
        package_name='pandas', module_name='Index')
    _verify_setop_compatible('intersection', I, other)
    bds__hywti = get_index_constructor(I) if not isinstance(I, RangeIndexType
        ) else init_numeric_index

    def impl(I, other, sort=None):
        jdsv__rdb = bodo.utils.conversion.coerce_to_array(I)
        zar__tfy = bodo.utils.conversion.coerce_to_array(other)
        iinlh__kmuw = bodo.libs.array_kernels.unique(jdsv__rdb)
        wfi__ydum = bodo.libs.array_kernels.unique(zar__tfy)
        gyzvi__vti = bodo.libs.array_kernels.concat([iinlh__kmuw, wfi__ydum])
        duzoh__bsv = pd.Series(gyzvi__vti).sort_values().values
        see__ctk = bodo.libs.array_kernels.intersection_mask(duzoh__bsv)
        return bds__hywti(duzoh__bsv[see__ctk], None)
    return impl


@overload_method(NumericIndexType, 'difference', inline='always')
@overload_method(StringIndexType, 'difference', inline='always')
@overload_method(BinaryIndexType, 'difference', inline='always')
@overload_method(DatetimeIndexType, 'difference', inline='always')
@overload_method(TimedeltaIndexType, 'difference', inline='always')
@overload_method(RangeIndexType, 'difference', inline='always')
def overload_index_difference(I, other, sort=None):
    grdlp__pza = dict(sort=sort)
    qvhp__whkh = dict(sort=None)
    check_unsupported_args('Index.difference', grdlp__pza, qvhp__whkh,
        package_name='pandas', module_name='Index')
    _verify_setop_compatible('difference', I, other)
    bds__hywti = get_index_constructor(I) if not isinstance(I, RangeIndexType
        ) else init_numeric_index

    def impl(I, other, sort=None):
        jdsv__rdb = bodo.utils.conversion.coerce_to_array(I)
        zar__tfy = bodo.utils.conversion.coerce_to_array(other)
        iinlh__kmuw = bodo.libs.array_kernels.unique(jdsv__rdb)
        wfi__ydum = bodo.libs.array_kernels.unique(zar__tfy)
        see__ctk = np.empty(len(iinlh__kmuw), np.bool_)
        bodo.libs.array.array_isin(see__ctk, iinlh__kmuw, wfi__ydum, False)
        return bds__hywti(iinlh__kmuw[~see__ctk], None)
    return impl


@overload_method(NumericIndexType, 'symmetric_difference', inline='always')
@overload_method(StringIndexType, 'symmetric_difference', inline='always')
@overload_method(BinaryIndexType, 'symmetric_difference', inline='always')
@overload_method(DatetimeIndexType, 'symmetric_difference', inline='always')
@overload_method(TimedeltaIndexType, 'symmetric_difference', inline='always')
@overload_method(RangeIndexType, 'symmetric_difference', inline='always')
def overload_index_symmetric_difference(I, other, result_name=None, sort=None):
    grdlp__pza = dict(result_name=result_name, sort=sort)
    qvhp__whkh = dict(result_name=None, sort=None)
    check_unsupported_args('Index.symmetric_difference', grdlp__pza,
        qvhp__whkh, package_name='pandas', module_name='Index')
    _verify_setop_compatible('symmetric_difference', I, other)
    bds__hywti = get_index_constructor(I) if not isinstance(I, RangeIndexType
        ) else init_numeric_index

    def impl(I, other, result_name=None, sort=None):
        jdsv__rdb = bodo.utils.conversion.coerce_to_array(I)
        zar__tfy = bodo.utils.conversion.coerce_to_array(other)
        iinlh__kmuw = bodo.libs.array_kernels.unique(jdsv__rdb)
        wfi__ydum = bodo.libs.array_kernels.unique(zar__tfy)
        kthg__uhp = np.empty(len(iinlh__kmuw), np.bool_)
        fixnq__jefdb = np.empty(len(wfi__ydum), np.bool_)
        bodo.libs.array.array_isin(kthg__uhp, iinlh__kmuw, wfi__ydum, False)
        bodo.libs.array.array_isin(fixnq__jefdb, wfi__ydum, iinlh__kmuw, False)
        pwadu__wlxb = bodo.libs.array_kernels.concat([iinlh__kmuw[~
            kthg__uhp], wfi__ydum[~fixnq__jefdb]])
        return bds__hywti(pwadu__wlxb, None)
    return impl


@overload_method(RangeIndexType, 'take', no_unliteral=True)
@overload_method(NumericIndexType, 'take', no_unliteral=True)
@overload_method(StringIndexType, 'take', no_unliteral=True)
@overload_method(BinaryIndexType, 'take', no_unliteral=True)
@overload_method(CategoricalIndexType, 'take', no_unliteral=True)
@overload_method(PeriodIndexType, 'take', no_unliteral=True)
@overload_method(DatetimeIndexType, 'take', no_unliteral=True)
@overload_method(TimedeltaIndexType, 'take', no_unliteral=True)
def overload_index_take(I, indices, axis=0, allow_fill=True, fill_value=None):
    grdlp__pza = dict(axis=axis, allow_fill=allow_fill, fill_value=fill_value)
    qvhp__whkh = dict(axis=0, allow_fill=True, fill_value=None)
    check_unsupported_args('Index.take', grdlp__pza, qvhp__whkh,
        package_name='pandas', module_name='Index')
    return lambda I, indices: I[indices]


def _init_engine(I, ban_unique=True):
    pass


@overload(_init_engine)
def overload_init_engine(I, ban_unique=True):
    if isinstance(I, CategoricalIndexType):

        def impl(I, ban_unique=True):
            if len(I) > 0 and not I._dict:
                owj__szc = bodo.utils.conversion.coerce_to_array(I)
                for i in range(len(owj__szc)):
                    if not bodo.libs.array_kernels.isna(owj__szc, i):
                        val = (bodo.hiframes.pd_categorical_ext.
                            get_code_for_value(owj__szc.dtype, owj__szc[i]))
                        if ban_unique and val in I._dict:
                            raise ValueError(
                                'Index.get_loc(): non-unique Index not supported yet'
                                )
                        I._dict[val] = i
        return impl
    else:

        def impl(I, ban_unique=True):
            if len(I) > 0 and not I._dict:
                owj__szc = bodo.utils.conversion.coerce_to_array(I)
                for i in range(len(owj__szc)):
                    if not bodo.libs.array_kernels.isna(owj__szc, i):
                        val = owj__szc[i]
                        if ban_unique and val in I._dict:
                            raise ValueError(
                                'Index.get_loc(): non-unique Index not supported yet'
                                )
                        I._dict[val] = i
        return impl


@overload(operator.contains, no_unliteral=True)
def index_contains(I, val):
    if not is_index_type(I):
        return
    if isinstance(I, RangeIndexType):
        return lambda I, val: range_contains(I.start, I.stop, I.step, val)
    if isinstance(I, CategoricalIndexType):

        def impl(I, val):
            key = bodo.utils.conversion.unbox_if_timestamp(val)
            if not is_null_value(I._dict):
                _init_engine(I, False)
                owj__szc = bodo.utils.conversion.coerce_to_array(I)
                fap__axbx = (bodo.hiframes.pd_categorical_ext.
                    get_code_for_value(owj__szc.dtype, key))
                return fap__axbx in I._dict
            else:
                wgb__swngk = (
                    'Global Index objects can be slow (pass as argument to JIT function for better performance).'
                    )
                warnings.warn(wgb__swngk)
                owj__szc = bodo.utils.conversion.coerce_to_array(I)
                ind = -1
                for i in range(len(owj__szc)):
                    if not bodo.libs.array_kernels.isna(owj__szc, i):
                        if owj__szc[i] == key:
                            ind = i
            return ind != -1
        return impl

    def impl(I, val):
        key = bodo.utils.conversion.unbox_if_timestamp(val)
        if not is_null_value(I._dict):
            _init_engine(I, False)
            return key in I._dict
        else:
            wgb__swngk = (
                'Global Index objects can be slow (pass as argument to JIT function for better performance).'
                )
            warnings.warn(wgb__swngk)
            owj__szc = bodo.utils.conversion.coerce_to_array(I)
            ind = -1
            for i in range(len(owj__szc)):
                if not bodo.libs.array_kernels.isna(owj__szc, i):
                    if owj__szc[i] == key:
                        ind = i
        return ind != -1
    return impl


@register_jitable
def range_contains(start, stop, step, val):
    if step > 0 and not start <= val < stop:
        return False
    if step < 0 and not stop <= val < start:
        return False
    return (val - start) % step == 0


@overload_method(RangeIndexType, 'get_loc', no_unliteral=True)
@overload_method(NumericIndexType, 'get_loc', no_unliteral=True)
@overload_method(StringIndexType, 'get_loc', no_unliteral=True)
@overload_method(BinaryIndexType, 'get_loc', no_unliteral=True)
@overload_method(PeriodIndexType, 'get_loc', no_unliteral=True)
@overload_method(DatetimeIndexType, 'get_loc', no_unliteral=True)
@overload_method(TimedeltaIndexType, 'get_loc', no_unliteral=True)
def overload_index_get_loc(I, key, method=None, tolerance=None):
    grdlp__pza = dict(method=method, tolerance=tolerance)
    bdenf__mso = dict(method=None, tolerance=None)
    check_unsupported_args('Index.get_loc', grdlp__pza, bdenf__mso,
        package_name='pandas', module_name='Index')
    key = types.unliteral(key)
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(I,
        'DatetimeIndex.get_loc')
    if key == pd_timestamp_type:
        key = bodo.datetime64ns
    if key == pd_timedelta_type:
        key = bodo.timedelta64ns
    if key != I.dtype:
        raise_bodo_error(
            'Index.get_loc(): invalid label type in Index.get_loc()')
    if isinstance(I, RangeIndexType):

        def impl_range(I, key, method=None, tolerance=None):
            if not range_contains(I.start, I.stop, I.step, key):
                raise KeyError('Index.get_loc(): key not found')
            return key - I.start if I.step == 1 else (key - I.start) // I.step
        return impl_range

    def impl(I, key, method=None, tolerance=None):
        key = bodo.utils.conversion.unbox_if_timestamp(key)
        if not is_null_value(I._dict):
            _init_engine(I)
            ind = I._dict.get(key, -1)
        else:
            wgb__swngk = (
                'Index.get_loc() can be slow for global Index objects (pass as argument to JIT function for better performance).'
                )
            warnings.warn(wgb__swngk)
            owj__szc = bodo.utils.conversion.coerce_to_array(I)
            ind = -1
            for i in range(len(owj__szc)):
                if owj__szc[i] == key:
                    if ind != -1:
                        raise ValueError(
                            'Index.get_loc(): non-unique Index not supported yet'
                            )
                    ind = i
        if ind == -1:
            raise KeyError('Index.get_loc(): key not found')
        return ind
    return impl


def create_isna_specific_method(overload_name):

    def overload_index_isna_specific_method(I):
        jilc__sghqx = overload_name in {'isna', 'isnull'}
        if isinstance(I, RangeIndexType):

            def impl(I):
                numba.parfors.parfor.init_prange()
                syi__wdj = len(I)
                qaob__oea = np.empty(syi__wdj, np.bool_)
                for i in numba.parfors.parfor.internal_prange(syi__wdj):
                    qaob__oea[i] = not jilc__sghqx
                return qaob__oea
            return impl
        ncl__uyeu = f"""def impl(I):
    numba.parfors.parfor.init_prange()
    arr = bodo.hiframes.pd_index_ext.get_index_data(I)
    n = len(arr)
    out_arr = np.empty(n, np.bool_)
    for i in numba.parfors.parfor.internal_prange(n):
       out_arr[i] = {'' if jilc__sghqx else 'not '}bodo.libs.array_kernels.isna(arr, i)
    return out_arr
"""
        iqmgk__pwkj = {}
        exec(ncl__uyeu, {'bodo': bodo, 'np': np, 'numba': numba}, iqmgk__pwkj)
        impl = iqmgk__pwkj['impl']
        return impl
    return overload_index_isna_specific_method


isna_overload_types = (RangeIndexType, NumericIndexType, StringIndexType,
    BinaryIndexType, CategoricalIndexType, PeriodIndexType,
    DatetimeIndexType, TimedeltaIndexType)
isna_specific_methods = 'isna', 'notna', 'isnull', 'notnull'


def _install_isna_specific_methods():
    for zpo__pzjkh in isna_overload_types:
        for overload_name in isna_specific_methods:
            overload_impl = create_isna_specific_method(overload_name)
            overload_method(zpo__pzjkh, overload_name, no_unliteral=True,
                inline='always')(overload_impl)


_install_isna_specific_methods()


@overload_attribute(RangeIndexType, 'values')
@overload_attribute(NumericIndexType, 'values')
@overload_attribute(StringIndexType, 'values')
@overload_attribute(BinaryIndexType, 'values')
@overload_attribute(CategoricalIndexType, 'values')
@overload_attribute(PeriodIndexType, 'values')
@overload_attribute(DatetimeIndexType, 'values')
@overload_attribute(TimedeltaIndexType, 'values')
def overload_values(I):
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(I, 'Index.values'
        )
    return lambda I: bodo.utils.conversion.coerce_to_array(I)


@overload(len, no_unliteral=True)
def overload_index_len(I):
    if isinstance(I, (NumericIndexType, StringIndexType, BinaryIndexType,
        PeriodIndexType, IntervalIndexType, CategoricalIndexType,
        DatetimeIndexType, TimedeltaIndexType, HeterogeneousIndexType)):
        return lambda I: len(bodo.hiframes.pd_index_ext.get_index_data(I))


@overload(len, no_unliteral=True)
def overload_multi_index_len(I):
    if isinstance(I, MultiIndexType):
        return lambda I: len(bodo.hiframes.pd_index_ext.get_index_data(I)[0])


@overload_attribute(DatetimeIndexType, 'shape')
@overload_attribute(NumericIndexType, 'shape')
@overload_attribute(StringIndexType, 'shape')
@overload_attribute(BinaryIndexType, 'shape')
@overload_attribute(PeriodIndexType, 'shape')
@overload_attribute(TimedeltaIndexType, 'shape')
@overload_attribute(IntervalIndexType, 'shape')
@overload_attribute(CategoricalIndexType, 'shape')
def overload_index_shape(s):
    return lambda s: (len(bodo.hiframes.pd_index_ext.get_index_data(s)),)


@overload_attribute(RangeIndexType, 'shape')
def overload_range_index_shape(s):
    return lambda s: (len(s),)


@overload_attribute(MultiIndexType, 'shape')
def overload_index_shape(s):
    return lambda s: (len(bodo.hiframes.pd_index_ext.get_index_data(s)[0]),)


@overload_attribute(NumericIndexType, 'is_monotonic', inline='always')
@overload_attribute(RangeIndexType, 'is_monotonic', inline='always')
@overload_attribute(DatetimeIndexType, 'is_monotonic', inline='always')
@overload_attribute(TimedeltaIndexType, 'is_monotonic', inline='always')
@overload_attribute(NumericIndexType, 'is_monotonic_increasing', inline=
    'always')
@overload_attribute(RangeIndexType, 'is_monotonic_increasing', inline='always')
@overload_attribute(DatetimeIndexType, 'is_monotonic_increasing', inline=
    'always')
@overload_attribute(TimedeltaIndexType, 'is_monotonic_increasing', inline=
    'always')
def overload_index_is_montonic(I):
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(I,
        'Index.is_monotonic_increasing')
    if isinstance(I, (NumericIndexType, DatetimeIndexType, TimedeltaIndexType)
        ):

        def impl(I):
            owj__szc = bodo.hiframes.pd_index_ext.get_index_data(I)
            return bodo.libs.array_kernels.series_monotonicity(owj__szc, 1)
        return impl
    elif isinstance(I, RangeIndexType):

        def impl(I):
            return I._step > 0 or len(I) <= 1
        return impl


@overload_attribute(NumericIndexType, 'is_monotonic_decreasing', inline=
    'always')
@overload_attribute(RangeIndexType, 'is_monotonic_decreasing', inline='always')
@overload_attribute(DatetimeIndexType, 'is_monotonic_decreasing', inline=
    'always')
@overload_attribute(TimedeltaIndexType, 'is_monotonic_decreasing', inline=
    'always')
def overload_index_is_montonic_decreasing(I):
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(I,
        'Index.is_monotonic_decreasing')
    if isinstance(I, (NumericIndexType, DatetimeIndexType, TimedeltaIndexType)
        ):

        def impl(I):
            owj__szc = bodo.hiframes.pd_index_ext.get_index_data(I)
            return bodo.libs.array_kernels.series_monotonicity(owj__szc, 2)
        return impl
    elif isinstance(I, RangeIndexType):

        def impl(I):
            return I._step < 0 or len(I) <= 1
        return impl


@overload_method(NumericIndexType, 'duplicated', inline='always',
    no_unliteral=True)
@overload_method(DatetimeIndexType, 'duplicated', inline='always',
    no_unliteral=True)
@overload_method(TimedeltaIndexType, 'duplicated', inline='always',
    no_unliteral=True)
@overload_method(StringIndexType, 'duplicated', inline='always',
    no_unliteral=True)
@overload_method(PeriodIndexType, 'duplicated', inline='always',
    no_unliteral=True)
@overload_method(CategoricalIndexType, 'duplicated', inline='always',
    no_unliteral=True)
@overload_method(BinaryIndexType, 'duplicated', inline='always',
    no_unliteral=True)
@overload_method(RangeIndexType, 'duplicated', inline='always',
    no_unliteral=True)
def overload_index_duplicated(I, keep='first'):
    if isinstance(I, RangeIndexType):

        def impl(I, keep='first'):
            return np.zeros(len(I), np.bool_)
        return impl

    def impl(I, keep='first'):
        owj__szc = bodo.hiframes.pd_index_ext.get_index_data(I)
        qaob__oea = bodo.libs.array_kernels.duplicated((owj__szc,))
        return qaob__oea
    return impl


@overload_method(NumericIndexType, 'any', no_unliteral=True, inline='always')
@overload_method(StringIndexType, 'any', no_unliteral=True, inline='always')
@overload_method(BinaryIndexType, 'any', no_unliteral=True, inline='always')
@overload_method(RangeIndexType, 'any', no_unliteral=True, inline='always')
def overload_index_any(I):
    if isinstance(I, RangeIndexType):

        def impl(I):
            return len(I) > 0 and (I._start != 0 or len(I) > 1)
        return impl

    def impl(I):
        A = bodo.hiframes.pd_index_ext.get_index_data(I)
        return bodo.libs.array_ops.array_op_any(A)
    return impl


@overload_method(NumericIndexType, 'all', no_unliteral=True, inline='always')
@overload_method(StringIndexType, 'all', no_unliteral=True, inline='always')
@overload_method(RangeIndexType, 'all', no_unliteral=True, inline='always')
@overload_method(BinaryIndexType, 'all', no_unliteral=True, inline='always')
def overload_index_all(I):
    if isinstance(I, RangeIndexType):

        def impl(I):
            return len(I) == 0 or I._step > 0 and (I._start > 0 or I._stop <= 0
                ) or I._step < 0 and (I._start < 0 or I._stop >= 0
                ) or I._start % I._step != 0
        return impl

    def impl(I):
        A = bodo.hiframes.pd_index_ext.get_index_data(I)
        return bodo.libs.array_ops.array_op_all(A)
    return impl


@overload_method(RangeIndexType, 'drop_duplicates', no_unliteral=True,
    inline='always')
@overload_method(NumericIndexType, 'drop_duplicates', no_unliteral=True,
    inline='always')
@overload_method(StringIndexType, 'drop_duplicates', no_unliteral=True,
    inline='always')
@overload_method(BinaryIndexType, 'drop_duplicates', no_unliteral=True,
    inline='always')
@overload_method(CategoricalIndexType, 'drop_duplicates', no_unliteral=True,
    inline='always')
@overload_method(PeriodIndexType, 'drop_duplicates', no_unliteral=True,
    inline='always')
@overload_method(DatetimeIndexType, 'drop_duplicates', no_unliteral=True,
    inline='always')
@overload_method(TimedeltaIndexType, 'drop_duplicates', no_unliteral=True,
    inline='always')
def overload_index_drop_duplicates(I, keep='first'):
    grdlp__pza = dict(keep=keep)
    bdenf__mso = dict(keep='first')
    check_unsupported_args('Index.drop_duplicates', grdlp__pza, bdenf__mso,
        package_name='pandas', module_name='Index')
    if isinstance(I, RangeIndexType):
        return lambda I, keep='first': I.copy()
    ncl__uyeu = """def impl(I, keep='first'):
    data = bodo.hiframes.pd_index_ext.get_index_data(I)
    arr = bodo.libs.array_kernels.drop_duplicates_array(data)
    name = bodo.hiframes.pd_index_ext.get_index_name(I)
"""
    if isinstance(I, PeriodIndexType):
        ncl__uyeu += f"""    return bodo.hiframes.pd_index_ext.init_period_index(arr, name, '{I.freq}')
"""
    else:
        ncl__uyeu += (
            '    return bodo.utils.conversion.index_from_array(arr, name)')
    iqmgk__pwkj = {}
    exec(ncl__uyeu, {'bodo': bodo}, iqmgk__pwkj)
    impl = iqmgk__pwkj['impl']
    return impl


@numba.generated_jit(nopython=True)
def get_index_data(S):
    return lambda S: S._data


@numba.generated_jit(nopython=True)
def get_index_name(S):
    return lambda S: S._name


def alias_ext_dummy_func(lhs_name, args, alias_map, arg_aliases):
    assert len(args) >= 1
    numba.core.ir_utils._add_alias(lhs_name, args[0].name, alias_map,
        arg_aliases)


numba.core.ir_utils.alias_func_extensions['get_index_data',
    'bodo.hiframes.pd_index_ext'] = alias_ext_dummy_func
numba.core.ir_utils.alias_func_extensions['init_datetime_index',
    'bodo.hiframes.pd_index_ext'] = alias_ext_dummy_func
numba.core.ir_utils.alias_func_extensions['init_timedelta_index',
    'bodo.hiframes.pd_index_ext'] = alias_ext_dummy_func
numba.core.ir_utils.alias_func_extensions['init_numeric_index',
    'bodo.hiframes.pd_index_ext'] = alias_ext_dummy_func
numba.core.ir_utils.alias_func_extensions['init_binary_str_index',
    'bodo.hiframes.pd_index_ext'] = alias_ext_dummy_func
numba.core.ir_utils.alias_func_extensions['init_categorical_index',
    'bodo.hiframes.pd_index_ext'] = alias_ext_dummy_func


def get_index_data_equiv(self, scope, equiv_set, loc, args, kws):
    assert len(args) == 1 and not kws
    qtsmd__ptmx = args[0]
    if isinstance(self.typemap[qtsmd__ptmx.name], (HeterogeneousIndexType,
        MultiIndexType)):
        return None
    if equiv_set.has_shape(qtsmd__ptmx):
        return ArrayAnalysis.AnalyzeResult(shape=qtsmd__ptmx, pre=[])
    return None


(ArrayAnalysis._analyze_op_call_bodo_hiframes_pd_index_ext_get_index_data
    ) = get_index_data_equiv


@overload_method(RangeIndexType, 'map', inline='always', no_unliteral=True)
@overload_method(NumericIndexType, 'map', inline='always', no_unliteral=True)
@overload_method(StringIndexType, 'map', inline='always', no_unliteral=True)
@overload_method(BinaryIndexType, 'map', inline='always', no_unliteral=True)
@overload_method(CategoricalIndexType, 'map', inline='always', no_unliteral
    =True)
@overload_method(PeriodIndexType, 'map', inline='always', no_unliteral=True)
@overload_method(DatetimeIndexType, 'map', inline='always', no_unliteral=True)
@overload_method(TimedeltaIndexType, 'map', inline='always', no_unliteral=True)
def overload_index_map(I, mapper, na_action=None):
    if not is_const_func_type(mapper):
        raise BodoError("Index.map(): 'mapper' should be a function")
    grdlp__pza = dict(na_action=na_action)
    yqzz__hrwb = dict(na_action=None)
    check_unsupported_args('Index.map', grdlp__pza, yqzz__hrwb,
        package_name='pandas', module_name='Index')
    dtype = I.dtype
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(I,
        'DatetimeIndex.map')
    if dtype == types.NPDatetime('ns'):
        dtype = pd_timestamp_type
    if dtype == types.NPTimedelta('ns'):
        dtype = pd_timedelta_type
    if isinstance(dtype, bodo.hiframes.pd_categorical_ext.PDCategoricalDtype):
        dtype = dtype.elem_type
    raf__tvux = numba.core.registry.cpu_target.typing_context
    apuzs__ntbn = numba.core.registry.cpu_target.target_context
    try:
        pthy__mglj = get_const_func_output_type(mapper, (dtype,), {},
            raf__tvux, apuzs__ntbn)
    except Exception as cvuwr__tqzq:
        raise_bodo_error(get_udf_error_msg('Index.map()', cvuwr__tqzq))
    kfxk__kkoat = get_udf_out_arr_type(pthy__mglj)
    func = get_overload_const_func(mapper, None)
    ncl__uyeu = 'def f(I, mapper, na_action=None):\n'
    ncl__uyeu += '  name = bodo.hiframes.pd_index_ext.get_index_name(I)\n'
    ncl__uyeu += '  A = bodo.utils.conversion.coerce_to_array(I)\n'
    ncl__uyeu += '  numba.parfors.parfor.init_prange()\n'
    ncl__uyeu += '  n = len(A)\n'
    ncl__uyeu += '  S = bodo.utils.utils.alloc_type(n, _arr_typ, (-1,))\n'
    ncl__uyeu += '  for i in numba.parfors.parfor.internal_prange(n):\n'
    ncl__uyeu += '    t2 = bodo.utils.conversion.box_if_dt64(A[i])\n'
    ncl__uyeu += '    v = map_func(t2)\n'
    ncl__uyeu += '    S[i] = bodo.utils.conversion.unbox_if_timestamp(v)\n'
    ncl__uyeu += '  return bodo.utils.conversion.index_from_array(S, name)\n'
    yziu__gkd = bodo.compiler.udf_jit(func)
    iqmgk__pwkj = {}
    exec(ncl__uyeu, {'numba': numba, 'np': np, 'pd': pd, 'bodo': bodo,
        'map_func': yziu__gkd, '_arr_typ': kfxk__kkoat,
        'init_nested_counts': bodo.utils.indexing.init_nested_counts,
        'add_nested_counts': bodo.utils.indexing.add_nested_counts,
        'data_arr_type': kfxk__kkoat.dtype}, iqmgk__pwkj)
    f = iqmgk__pwkj['f']
    return f


@lower_builtin(operator.is_, NumericIndexType, NumericIndexType)
@lower_builtin(operator.is_, StringIndexType, StringIndexType)
@lower_builtin(operator.is_, BinaryIndexType, BinaryIndexType)
@lower_builtin(operator.is_, PeriodIndexType, PeriodIndexType)
@lower_builtin(operator.is_, DatetimeIndexType, DatetimeIndexType)
@lower_builtin(operator.is_, TimedeltaIndexType, TimedeltaIndexType)
@lower_builtin(operator.is_, IntervalIndexType, IntervalIndexType)
@lower_builtin(operator.is_, CategoricalIndexType, CategoricalIndexType)
def index_is(context, builder, sig, args):
    kjrv__qata, yxu__pft = sig.args
    if kjrv__qata != yxu__pft:
        return cgutils.false_bit

    def index_is_impl(a, b):
        return a._data is b._data and a._name is b._name
    return context.compile_internal(builder, index_is_impl, sig, args)


@lower_builtin(operator.is_, RangeIndexType, RangeIndexType)
def range_index_is(context, builder, sig, args):
    kjrv__qata, yxu__pft = sig.args
    if kjrv__qata != yxu__pft:
        return cgutils.false_bit

    def index_is_impl(a, b):
        return (a._start == b._start and a._stop == b._stop and a._step ==
            b._step and a._name is b._name)
    return context.compile_internal(builder, index_is_impl, sig, args)


def create_binary_op_overload(op):

    def overload_index_binary_op(lhs, rhs):
        if is_index_type(lhs):
            ncl__uyeu = (
                'def impl(lhs, rhs):\n  arr = bodo.utils.conversion.coerce_to_array(lhs)\n'
                )
            if rhs in [bodo.hiframes.pd_timestamp_ext.pd_timestamp_type,
                bodo.hiframes.pd_timestamp_ext.pd_timedelta_type]:
                ncl__uyeu += """  dt = bodo.utils.conversion.unbox_if_timestamp(rhs)
  return op(arr, dt)
"""
            else:
                ncl__uyeu += """  rhs_arr = bodo.utils.conversion.get_array_if_series_or_index(rhs)
  return op(arr, rhs_arr)
"""
            iqmgk__pwkj = {}
            exec(ncl__uyeu, {'bodo': bodo, 'op': op}, iqmgk__pwkj)
            impl = iqmgk__pwkj['impl']
            return impl
        if is_index_type(rhs):
            ncl__uyeu = (
                'def impl(lhs, rhs):\n  arr = bodo.utils.conversion.coerce_to_array(rhs)\n'
                )
            if lhs in [bodo.hiframes.pd_timestamp_ext.pd_timestamp_type,
                bodo.hiframes.pd_timestamp_ext.pd_timedelta_type]:
                ncl__uyeu += """  dt = bodo.utils.conversion.unbox_if_timestamp(lhs)
  return op(dt, arr)
"""
            else:
                ncl__uyeu += """  lhs_arr = bodo.utils.conversion.get_array_if_series_or_index(lhs)
  return op(lhs_arr, arr)
"""
            iqmgk__pwkj = {}
            exec(ncl__uyeu, {'bodo': bodo, 'op': op}, iqmgk__pwkj)
            impl = iqmgk__pwkj['impl']
            return impl
        if isinstance(lhs, HeterogeneousIndexType):
            if not is_heterogeneous_tuple_type(lhs.data):

                def impl3(lhs, rhs):
                    data = bodo.utils.conversion.coerce_to_array(lhs)
                    owj__szc = bodo.utils.conversion.coerce_to_array(data)
                    lfytk__lhxpn = (bodo.utils.conversion.
                        get_array_if_series_or_index(rhs))
                    qaob__oea = op(owj__szc, lfytk__lhxpn)
                    return qaob__oea
                return impl3
            count = len(lhs.data.types)
            ncl__uyeu = 'def f(lhs, rhs):\n'
            ncl__uyeu += '  return [{}]\n'.format(','.join(
                'op(lhs[{}], rhs{})'.format(i, f'[{i}]' if is_iterable_type
                (rhs) else '') for i in range(count)))
            iqmgk__pwkj = {}
            exec(ncl__uyeu, {'op': op, 'np': np}, iqmgk__pwkj)
            impl = iqmgk__pwkj['f']
            return impl
        if isinstance(rhs, HeterogeneousIndexType):
            if not is_heterogeneous_tuple_type(rhs.data):

                def impl4(lhs, rhs):
                    data = bodo.hiframes.pd_index_ext.get_index_data(rhs)
                    owj__szc = bodo.utils.conversion.coerce_to_array(data)
                    lfytk__lhxpn = (bodo.utils.conversion.
                        get_array_if_series_or_index(lhs))
                    qaob__oea = op(lfytk__lhxpn, owj__szc)
                    return qaob__oea
                return impl4
            count = len(rhs.data.types)
            ncl__uyeu = 'def f(lhs, rhs):\n'
            ncl__uyeu += '  return [{}]\n'.format(','.join(
                'op(lhs{}, rhs[{}])'.format(f'[{i}]' if is_iterable_type(
                lhs) else '', i) for i in range(count)))
            iqmgk__pwkj = {}
            exec(ncl__uyeu, {'op': op, 'np': np}, iqmgk__pwkj)
            impl = iqmgk__pwkj['f']
            return impl
    return overload_index_binary_op


skips = [operator.lt, operator.le, operator.eq, operator.ne, operator.gt,
    operator.ge, operator.add, operator.sub, operator.mul, operator.truediv,
    operator.floordiv, operator.pow, operator.mod]


def _install_binary_ops():
    for op in bodo.hiframes.pd_series_ext.series_binary_ops:
        if op in skips:
            continue
        overload_impl = create_binary_op_overload(op)
        overload(op, inline='always')(overload_impl)


_install_binary_ops()


def is_index_type(t):
    return isinstance(t, (RangeIndexType, NumericIndexType, StringIndexType,
        BinaryIndexType, PeriodIndexType, DatetimeIndexType,
        TimedeltaIndexType, IntervalIndexType, CategoricalIndexType))


@lower_cast(RangeIndexType, NumericIndexType)
def cast_range_index_to_int_index(context, builder, fromty, toty, val):
    f = lambda I: init_numeric_index(np.arange(I._start, I._stop, I._step),
        bodo.hiframes.pd_index_ext.get_index_name(I))
    return context.compile_internal(builder, f, toty(fromty), [val])


@numba.njit(no_cpython_wrapper=True)
def range_index_to_numeric(I):
    return init_numeric_index(np.arange(I._start, I._stop, I._step), bodo.
        hiframes.pd_index_ext.get_index_name(I))


class HeterogeneousIndexType(types.Type):
    ndim = 1

    def __init__(self, data=None, name_typ=None):
        self.data = data
        name_typ = types.none if name_typ is None else name_typ
        self.name_typ = name_typ
        super(HeterogeneousIndexType, self).__init__(name=
            f'heter_index({data}, {name_typ})')

    def copy(self):
        return HeterogeneousIndexType(self.data, self.name_typ)

    @property
    def key(self):
        return self.data, self.name_typ

    @property
    def mangling_args(self):
        return self.__class__.__name__, (self._code,)

    @property
    def pandas_type_name(self):
        return 'object'

    @property
    def numpy_type_name(self):
        return 'object'


@register_model(HeterogeneousIndexType)
class HeterogeneousIndexModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        deo__qhjso = [('data', fe_type.data), ('name', fe_type.name_typ)]
        super(HeterogeneousIndexModel, self).__init__(dmm, fe_type, deo__qhjso)


make_attribute_wrapper(HeterogeneousIndexType, 'data', '_data')
make_attribute_wrapper(HeterogeneousIndexType, 'name', '_name')


@overload_method(HeterogeneousIndexType, 'copy', no_unliteral=True)
def overload_heter_index_copy(A, name=None, deep=False, dtype=None, names=None
    ):
    fyrwk__jmtv = idx_typ_to_format_str_map[HeterogeneousIndexType].format(
        'copy()')
    pdqh__twc = dict(deep=deep, dtype=dtype, names=names)
    check_unsupported_args('Index.copy', pdqh__twc, idx_cpy_arg_defaults,
        fn_str=fyrwk__jmtv, package_name='pandas', module_name='Index')
    if not is_overload_none(name):

        def impl(A, name=None, deep=False, dtype=None, names=None):
            return bodo.hiframes.pd_index_ext.init_numeric_index(A._data.
                copy(), name)
    else:

        def impl(A, name=None, deep=False, dtype=None, names=None):
            return bodo.hiframes.pd_index_ext.init_numeric_index(A._data.
                copy(), A._name)
    return impl


@box(HeterogeneousIndexType)
def box_heter_index(typ, val, c):
    mxm__uztw = c.context.insert_const_string(c.builder.module, 'pandas')
    gmsz__moqir = c.pyapi.import_module_noblock(mxm__uztw)
    waftq__ihx = cgutils.create_struct_proxy(typ)(c.context, c.builder, val)
    c.context.nrt.incref(c.builder, typ.data, waftq__ihx.data)
    jgeh__lwf = c.pyapi.from_native_value(typ.data, waftq__ihx.data, c.
        env_manager)
    c.context.nrt.incref(c.builder, typ.name_typ, waftq__ihx.name)
    fyqru__rsm = c.pyapi.from_native_value(typ.name_typ, waftq__ihx.name, c
        .env_manager)
    eipq__lrrkt = c.pyapi.make_none()
    dgief__tzzy = c.pyapi.bool_from_bool(c.context.get_constant(types.bool_,
        False))
    sigju__sgdcb = c.pyapi.call_method(gmsz__moqir, 'Index', (jgeh__lwf,
        eipq__lrrkt, dgief__tzzy, fyqru__rsm))
    c.pyapi.decref(jgeh__lwf)
    c.pyapi.decref(eipq__lrrkt)
    c.pyapi.decref(dgief__tzzy)
    c.pyapi.decref(fyqru__rsm)
    c.pyapi.decref(gmsz__moqir)
    c.context.nrt.decref(c.builder, typ, val)
    return sigju__sgdcb


@intrinsic
def init_heter_index(typingctx, data, name=None):
    name = types.none if name is None else name

    def codegen(context, builder, signature, args):
        assert len(args) == 2
        byo__wvsup = signature.return_type
        waftq__ihx = cgutils.create_struct_proxy(byo__wvsup)(context, builder)
        waftq__ihx.data = args[0]
        waftq__ihx.name = args[1]
        context.nrt.incref(builder, byo__wvsup.data, args[0])
        context.nrt.incref(builder, byo__wvsup.name_typ, args[1])
        return waftq__ihx._getvalue()
    return HeterogeneousIndexType(data, name)(data, name), codegen


@overload_attribute(HeterogeneousIndexType, 'name')
def heter_index_get_name(i):

    def impl(i):
        return i._name
    return impl


@overload_attribute(NumericIndexType, 'nbytes')
@overload_attribute(DatetimeIndexType, 'nbytes')
@overload_attribute(TimedeltaIndexType, 'nbytes')
@overload_attribute(RangeIndexType, 'nbytes')
@overload_attribute(StringIndexType, 'nbytes')
@overload_attribute(BinaryIndexType, 'nbytes')
@overload_attribute(CategoricalIndexType, 'nbytes')
@overload_attribute(PeriodIndexType, 'nbytes')
@overload_attribute(MultiIndexType, 'nbytes')
def overload_nbytes(I):
    if isinstance(I, RangeIndexType):

        def _impl_nbytes(I):
            return bodo.io.np_io.get_dtype_size(type(I._start)
                ) + bodo.io.np_io.get_dtype_size(type(I._step)
                ) + bodo.io.np_io.get_dtype_size(type(I._stop))
        return _impl_nbytes
    elif isinstance(I, MultiIndexType):
        ncl__uyeu = 'def _impl_nbytes(I):\n'
        ncl__uyeu += '    total = 0\n'
        ncl__uyeu += '    data = I._data\n'
        for i in range(I.nlevels):
            ncl__uyeu += f'    total += data[{i}].nbytes\n'
        ncl__uyeu += '    return total\n'
        heck__sxq = {}
        exec(ncl__uyeu, {}, heck__sxq)
        return heck__sxq['_impl_nbytes']
    else:

        def _impl_nbytes(I):
            return I._data.nbytes
        return _impl_nbytes


@overload_method(NumericIndexType, 'to_series', inline='always')
@overload_method(DatetimeIndexType, 'to_series', inline='always')
@overload_method(TimedeltaIndexType, 'to_series', inline='always')
@overload_method(RangeIndexType, 'to_series', inline='always')
@overload_method(StringIndexType, 'to_series', inline='always')
@overload_method(BinaryIndexType, 'to_series', inline='always')
@overload_method(CategoricalIndexType, 'to_series', inline='always')
def overload_index_to_series(I, index=None, name=None):
    if not (is_overload_constant_str(name) or is_overload_constant_int(name
        ) or is_overload_none(name)):
        raise_bodo_error(
            f'Index.to_series(): only constant string/int are supported for argument name'
            )
    if is_overload_none(name):
        nkon__ftlpi = 'bodo.hiframes.pd_index_ext.get_index_name(I)'
    else:
        nkon__ftlpi = 'name'
    ncl__uyeu = 'def impl(I, index=None, name=None):\n'
    ncl__uyeu += '    data = bodo.utils.conversion.index_to_array(I)\n'
    if is_overload_none(index):
        ncl__uyeu += '    new_index = I\n'
    elif is_pd_index_type(index):
        ncl__uyeu += '    new_index = index\n'
    elif isinstance(index, SeriesType):
        ncl__uyeu += '    arr = bodo.utils.conversion.coerce_to_array(index)\n'
        ncl__uyeu += (
            '    index_name = bodo.hiframes.pd_series_ext.get_series_name(index)\n'
            )
        ncl__uyeu += (
            '    new_index = bodo.utils.conversion.index_from_array(arr, index_name)\n'
            )
    elif bodo.utils.utils.is_array_typ(index, False):
        ncl__uyeu += (
            '    new_index = bodo.utils.conversion.index_from_array(index)\n')
    elif isinstance(index, (types.List, types.BaseTuple)):
        ncl__uyeu += '    arr = bodo.utils.conversion.coerce_to_array(index)\n'
        ncl__uyeu += (
            '    new_index = bodo.utils.conversion.index_from_array(arr)\n')
    else:
        raise_bodo_error(
            f'Index.to_series(): unsupported type for argument index: {type(index).__name__}'
            )
    ncl__uyeu += f'    new_name = {nkon__ftlpi}\n'
    ncl__uyeu += (
        '    return bodo.hiframes.pd_series_ext.init_series(data, new_index, new_name)'
        )
    iqmgk__pwkj = {}
    exec(ncl__uyeu, {'bodo': bodo, 'np': np}, iqmgk__pwkj)
    impl = iqmgk__pwkj['impl']
    return impl


@overload_method(NumericIndexType, 'to_frame', inline='always',
    no_unliteral=True)
@overload_method(DatetimeIndexType, 'to_frame', inline='always',
    no_unliteral=True)
@overload_method(TimedeltaIndexType, 'to_frame', inline='always',
    no_unliteral=True)
@overload_method(RangeIndexType, 'to_frame', inline='always', no_unliteral=True
    )
@overload_method(StringIndexType, 'to_frame', inline='always', no_unliteral
    =True)
@overload_method(BinaryIndexType, 'to_frame', inline='always', no_unliteral
    =True)
@overload_method(CategoricalIndexType, 'to_frame', inline='always',
    no_unliteral=True)
def overload_index_to_frame(I, index=True, name=None):
    if is_overload_true(index):
        mvtz__qaayr = 'I'
    elif is_overload_false(index):
        mvtz__qaayr = (
            'bodo.hiframes.pd_index_ext.init_range_index(0, len(I), 1, None)')
    elif not isinstance(index, types.Boolean):
        raise_bodo_error(
            'Index.to_frame(): index argument must be a constant boolean')
    else:
        raise_bodo_error(
            'Index.to_frame(): index argument must be a compile time constant')
    ncl__uyeu = 'def impl(I, index=True, name=None):\n'
    ncl__uyeu += '    data = bodo.utils.conversion.index_to_array(I)\n'
    ncl__uyeu += f'    new_index = {mvtz__qaayr}\n'
    if is_overload_none(name) and I.name_typ == types.none:
        fvwf__ygw = ColNamesMetaType((0,))
    elif is_overload_none(name):
        fvwf__ygw = ColNamesMetaType((I.name_typ,))
    elif is_overload_constant_str(name):
        fvwf__ygw = ColNamesMetaType((get_overload_const_str(name),))
    elif is_overload_constant_int(name):
        fvwf__ygw = ColNamesMetaType((get_overload_const_int(name),))
    else:
        raise_bodo_error(
            f'Index.to_frame(): only constant string/int are supported for argument name'
            )
    ncl__uyeu += """    return bodo.hiframes.pd_dataframe_ext.init_dataframe((data,), new_index, __col_name_meta_value)
"""
    iqmgk__pwkj = {}
    exec(ncl__uyeu, {'bodo': bodo, 'np': np, '__col_name_meta_value':
        fvwf__ygw}, iqmgk__pwkj)
    impl = iqmgk__pwkj['impl']
    return impl


@overload_method(MultiIndexType, 'to_frame', inline='always', no_unliteral=True
    )
def overload_multi_index_to_frame(I, index=True, name=None):
    if is_overload_true(index):
        mvtz__qaayr = 'I'
    elif is_overload_false(index):
        mvtz__qaayr = (
            'bodo.hiframes.pd_index_ext.init_range_index(0, len(I), 1, None)')
    elif not isinstance(index, types.Boolean):
        raise_bodo_error(
            'MultiIndex.to_frame(): index argument must be a constant boolean')
    else:
        raise_bodo_error(
            'MultiIndex.to_frame(): index argument must be a compile time constant'
            )
    ncl__uyeu = 'def impl(I, index=True, name=None):\n'
    ncl__uyeu += '    data = bodo.hiframes.pd_index_ext.get_index_data(I)\n'
    ncl__uyeu += f'    new_index = {mvtz__qaayr}\n'
    ezxiv__tbcvp = len(I.array_types)
    if is_overload_none(name) and I.names_typ == (types.none,) * ezxiv__tbcvp:
        fvwf__ygw = ColNamesMetaType(tuple(range(ezxiv__tbcvp)))
    elif is_overload_none(name):
        fvwf__ygw = ColNamesMetaType(I.names_typ)
    elif is_overload_constant_tuple(name) or is_overload_constant_list(name):
        if is_overload_constant_list(name):
            names = tuple(get_overload_const_list(name))
        else:
            names = get_overload_const_tuple(name)
        if ezxiv__tbcvp != len(names):
            raise_bodo_error(
                f'MultiIndex.to_frame(): expected {ezxiv__tbcvp} names, not {len(names)}'
                )
        if all(is_overload_constant_str(mjp__uts) or
            is_overload_constant_int(mjp__uts) for mjp__uts in names):
            fvwf__ygw = ColNamesMetaType(names)
        else:
            raise_bodo_error(
                'MultiIndex.to_frame(): only constant string/int list/tuple are supported for argument name'
                )
    else:
        raise_bodo_error(
            'MultiIndex.to_frame(): only constant string/int list/tuple are supported for argument name'
            )
    ncl__uyeu += """    return bodo.hiframes.pd_dataframe_ext.init_dataframe(data, new_index, __col_name_meta_value,)
"""
    iqmgk__pwkj = {}
    exec(ncl__uyeu, {'bodo': bodo, 'np': np, '__col_name_meta_value':
        fvwf__ygw}, iqmgk__pwkj)
    impl = iqmgk__pwkj['impl']
    return impl


@overload_method(NumericIndexType, 'to_numpy', inline='always')
@overload_method(DatetimeIndexType, 'to_numpy', inline='always')
@overload_method(TimedeltaIndexType, 'to_numpy', inline='always')
@overload_method(RangeIndexType, 'to_numpy', inline='always')
@overload_method(StringIndexType, 'to_numpy', inline='always')
@overload_method(BinaryIndexType, 'to_numpy', inline='always')
@overload_method(CategoricalIndexType, 'to_numpy', inline='always')
@overload_method(IntervalIndexType, 'to_numpy', inline='always')
def overload_index_to_numpy(I, dtype=None, copy=False, na_value=None):
    grdlp__pza = dict(dtype=dtype, na_value=na_value)
    bdenf__mso = dict(dtype=None, na_value=None)
    check_unsupported_args('Index.to_numpy', grdlp__pza, bdenf__mso,
        package_name='pandas', module_name='Index')
    if not is_overload_bool(copy):
        raise_bodo_error('Index.to_numpy(): copy argument must be a boolean')
    if isinstance(I, RangeIndexType):

        def impl(I, dtype=None, copy=False, na_value=None):
            return np.arange(I._start, I._stop, I._step)
        return impl
    if is_overload_true(copy):

        def impl(I, dtype=None, copy=False, na_value=None):
            return bodo.hiframes.pd_index_ext.get_index_data(I).copy()
        return impl
    if is_overload_false(copy):

        def impl(I, dtype=None, copy=False, na_value=None):
            return bodo.hiframes.pd_index_ext.get_index_data(I)
        return impl

    def impl(I, dtype=None, copy=False, na_value=None):
        data = bodo.hiframes.pd_index_ext.get_index_data(I)
        return data.copy() if copy else data
    return impl


@overload_method(NumericIndexType, 'to_list', inline='always')
@overload_method(RangeIndexType, 'to_list', inline='always')
@overload_method(StringIndexType, 'to_list', inline='always')
@overload_method(BinaryIndexType, 'to_list', inline='always')
@overload_method(CategoricalIndexType, 'to_list', inline='always')
@overload_method(DatetimeIndexType, 'to_list', inline='always')
@overload_method(TimedeltaIndexType, 'to_list', inline='always')
@overload_method(NumericIndexType, 'tolist', inline='always')
@overload_method(RangeIndexType, 'tolist', inline='always')
@overload_method(StringIndexType, 'tolist', inline='always')
@overload_method(BinaryIndexType, 'tolist', inline='always')
@overload_method(CategoricalIndexType, 'tolist', inline='always')
@overload_method(DatetimeIndexType, 'tolist', inline='always')
@overload_method(TimedeltaIndexType, 'tolist', inline='always')
def overload_index_to_list(I):
    if isinstance(I, RangeIndexType):

        def impl(I):
            gfgnd__gpy = list()
            for i in range(I._start, I._stop, I.step):
                gfgnd__gpy.append(i)
            return gfgnd__gpy
        return impl

    def impl(I):
        gfgnd__gpy = list()
        for i in range(len(I)):
            gfgnd__gpy.append(I[i])
        return gfgnd__gpy
    return impl


@overload_attribute(NumericIndexType, 'T')
@overload_attribute(DatetimeIndexType, 'T')
@overload_attribute(TimedeltaIndexType, 'T')
@overload_attribute(RangeIndexType, 'T')
@overload_attribute(StringIndexType, 'T')
@overload_attribute(BinaryIndexType, 'T')
@overload_attribute(CategoricalIndexType, 'T')
@overload_attribute(PeriodIndexType, 'T')
@overload_attribute(MultiIndexType, 'T')
@overload_attribute(IntervalIndexType, 'T')
def overload_T(I):
    return lambda I: I


@overload_attribute(NumericIndexType, 'size')
@overload_attribute(DatetimeIndexType, 'size')
@overload_attribute(TimedeltaIndexType, 'size')
@overload_attribute(RangeIndexType, 'size')
@overload_attribute(StringIndexType, 'size')
@overload_attribute(BinaryIndexType, 'size')
@overload_attribute(CategoricalIndexType, 'size')
@overload_attribute(PeriodIndexType, 'size')
@overload_attribute(MultiIndexType, 'size')
@overload_attribute(IntervalIndexType, 'size')
def overload_size(I):
    return lambda I: len(I)


@overload_attribute(NumericIndexType, 'ndim')
@overload_attribute(DatetimeIndexType, 'ndim')
@overload_attribute(TimedeltaIndexType, 'ndim')
@overload_attribute(RangeIndexType, 'ndim')
@overload_attribute(StringIndexType, 'ndim')
@overload_attribute(BinaryIndexType, 'ndim')
@overload_attribute(CategoricalIndexType, 'ndim')
@overload_attribute(PeriodIndexType, 'ndim')
@overload_attribute(MultiIndexType, 'ndim')
@overload_attribute(IntervalIndexType, 'ndim')
def overload_ndim(I):
    return lambda I: 1


@overload_attribute(NumericIndexType, 'nlevels')
@overload_attribute(DatetimeIndexType, 'nlevels')
@overload_attribute(TimedeltaIndexType, 'nlevels')
@overload_attribute(RangeIndexType, 'nlevels')
@overload_attribute(StringIndexType, 'nlevels')
@overload_attribute(BinaryIndexType, 'nlevels')
@overload_attribute(CategoricalIndexType, 'nlevels')
@overload_attribute(PeriodIndexType, 'nlevels')
@overload_attribute(MultiIndexType, 'nlevels')
@overload_attribute(IntervalIndexType, 'nlevels')
def overload_nlevels(I):
    if isinstance(I, MultiIndexType):
        return lambda I: len(I._data)
    return lambda I: 1


@overload_attribute(NumericIndexType, 'empty')
@overload_attribute(DatetimeIndexType, 'empty')
@overload_attribute(TimedeltaIndexType, 'empty')
@overload_attribute(RangeIndexType, 'empty')
@overload_attribute(StringIndexType, 'empty')
@overload_attribute(BinaryIndexType, 'empty')
@overload_attribute(CategoricalIndexType, 'empty')
@overload_attribute(PeriodIndexType, 'empty')
@overload_attribute(MultiIndexType, 'empty')
@overload_attribute(IntervalIndexType, 'empty')
def overload_empty(I):
    return lambda I: len(I) == 0


@overload_attribute(NumericIndexType, 'is_all_dates')
@overload_attribute(DatetimeIndexType, 'is_all_dates')
@overload_attribute(TimedeltaIndexType, 'is_all_dates')
@overload_attribute(RangeIndexType, 'is_all_dates')
@overload_attribute(StringIndexType, 'is_all_dates')
@overload_attribute(BinaryIndexType, 'is_all_dates')
@overload_attribute(CategoricalIndexType, 'is_all_dates')
@overload_attribute(PeriodIndexType, 'is_all_dates')
@overload_attribute(MultiIndexType, 'is_all_dates')
@overload_attribute(IntervalIndexType, 'is_all_dates')
def overload_is_all_dates(I):
    if isinstance(I, (DatetimeIndexType, TimedeltaIndexType, PeriodIndexType)):
        return lambda I: True
    else:
        return lambda I: False


@overload_attribute(NumericIndexType, 'inferred_type')
@overload_attribute(DatetimeIndexType, 'inferred_type')
@overload_attribute(TimedeltaIndexType, 'inferred_type')
@overload_attribute(RangeIndexType, 'inferred_type')
@overload_attribute(StringIndexType, 'inferred_type')
@overload_attribute(BinaryIndexType, 'inferred_type')
@overload_attribute(CategoricalIndexType, 'inferred_type')
@overload_attribute(PeriodIndexType, 'inferred_type')
@overload_attribute(MultiIndexType, 'inferred_type')
@overload_attribute(IntervalIndexType, 'inferred_type')
def overload_inferred_type(I):
    if isinstance(I, NumericIndexType):
        if isinstance(I.dtype, types.Integer):
            return lambda I: 'integer'
        elif isinstance(I.dtype, types.Float):
            return lambda I: 'floating'
        elif isinstance(I.dtype, types.Boolean):
            return lambda I: 'boolean'
        return
    if isinstance(I, StringIndexType):

        def impl(I):
            if len(I._data) == 0:
                return 'empty'
            return 'string'
        return impl
    htgfk__yemfb = {DatetimeIndexType: 'datetime64', TimedeltaIndexType:
        'timedelta64', RangeIndexType: 'integer', BinaryIndexType: 'bytes',
        CategoricalIndexType: 'categorical', PeriodIndexType: 'period',
        IntervalIndexType: 'interval', MultiIndexType: 'mixed'}
    inferred_type = htgfk__yemfb[type(I)]
    return lambda I: inferred_type


@overload_attribute(NumericIndexType, 'dtype')
@overload_attribute(DatetimeIndexType, 'dtype')
@overload_attribute(TimedeltaIndexType, 'dtype')
@overload_attribute(RangeIndexType, 'dtype')
@overload_attribute(StringIndexType, 'dtype')
@overload_attribute(BinaryIndexType, 'dtype')
@overload_attribute(CategoricalIndexType, 'dtype')
@overload_attribute(MultiIndexType, 'dtype')
def overload_inferred_type(I):
    if isinstance(I, NumericIndexType):
        if isinstance(I.dtype, types.Boolean):
            return lambda I: np.dtype('O')
        dtype = I.dtype
        return lambda I: dtype
    if isinstance(I, CategoricalIndexType):
        dtype = bodo.utils.utils.create_categorical_type(I.dtype.categories,
            I.data, I.dtype.ordered)
        return lambda I: dtype
    uijdn__lel = {DatetimeIndexType: np.dtype('datetime64[ns]'),
        TimedeltaIndexType: np.dtype('timedelta64[ns]'), RangeIndexType: np
        .dtype('int64'), StringIndexType: np.dtype('O'), BinaryIndexType:
        np.dtype('O'), MultiIndexType: np.dtype('O')}
    dtype = uijdn__lel[type(I)]
    return lambda I: dtype


@overload_attribute(NumericIndexType, 'names')
@overload_attribute(DatetimeIndexType, 'names')
@overload_attribute(TimedeltaIndexType, 'names')
@overload_attribute(RangeIndexType, 'names')
@overload_attribute(StringIndexType, 'names')
@overload_attribute(BinaryIndexType, 'names')
@overload_attribute(CategoricalIndexType, 'names')
@overload_attribute(IntervalIndexType, 'names')
@overload_attribute(PeriodIndexType, 'names')
@overload_attribute(MultiIndexType, 'names')
def overload_names(I):
    if isinstance(I, MultiIndexType):
        return lambda I: I._names
    return lambda I: (I._name,)


@overload_method(NumericIndexType, 'rename', inline='always')
@overload_method(DatetimeIndexType, 'rename', inline='always')
@overload_method(TimedeltaIndexType, 'rename', inline='always')
@overload_method(RangeIndexType, 'rename', inline='always')
@overload_method(StringIndexType, 'rename', inline='always')
@overload_method(BinaryIndexType, 'rename', inline='always')
@overload_method(CategoricalIndexType, 'rename', inline='always')
@overload_method(PeriodIndexType, 'rename', inline='always')
@overload_method(IntervalIndexType, 'rename', inline='always')
@overload_method(HeterogeneousIndexType, 'rename', inline='always')
def overload_rename(I, name, inplace=False):
    if is_overload_true(inplace):
        raise BodoError('Index.rename(): inplace index renaming unsupported')
    return init_index_from_index(I, name)


def init_index_from_index(I, name):
    bdor__jfl = {NumericIndexType: bodo.hiframes.pd_index_ext.
        init_numeric_index, DatetimeIndexType: bodo.hiframes.pd_index_ext.
        init_datetime_index, TimedeltaIndexType: bodo.hiframes.pd_index_ext
        .init_timedelta_index, StringIndexType: bodo.hiframes.pd_index_ext.
        init_binary_str_index, BinaryIndexType: bodo.hiframes.pd_index_ext.
        init_binary_str_index, CategoricalIndexType: bodo.hiframes.
        pd_index_ext.init_categorical_index, IntervalIndexType: bodo.
        hiframes.pd_index_ext.init_interval_index}
    if type(I) in bdor__jfl:
        init_func = bdor__jfl[type(I)]
        return lambda I, name, inplace=False: init_func(bodo.hiframes.
            pd_index_ext.get_index_data(I).copy(), name)
    if isinstance(I, RangeIndexType):
        return lambda I, name, inplace=False: I.copy(name=name)
    if isinstance(I, PeriodIndexType):
        freq = I.freq
        return (lambda I, name, inplace=False: bodo.hiframes.pd_index_ext.
            init_period_index(bodo.hiframes.pd_index_ext.get_index_data(I).
            copy(), name, freq))
    if isinstance(I, HeterogeneousIndexType):
        return (lambda I, name, inplace=False: bodo.hiframes.pd_index_ext.
            init_heter_index(bodo.hiframes.pd_index_ext.get_index_data(I),
            name))
    raise_bodo_error(f'init_index(): Unknown type {type(I)}')


def get_index_constructor(I):
    rsr__ysvx = {NumericIndexType: bodo.hiframes.pd_index_ext.
        init_numeric_index, DatetimeIndexType: bodo.hiframes.pd_index_ext.
        init_datetime_index, TimedeltaIndexType: bodo.hiframes.pd_index_ext
        .init_timedelta_index, StringIndexType: bodo.hiframes.pd_index_ext.
        init_binary_str_index, BinaryIndexType: bodo.hiframes.pd_index_ext.
        init_binary_str_index, CategoricalIndexType: bodo.hiframes.
        pd_index_ext.init_categorical_index, IntervalIndexType: bodo.
        hiframes.pd_index_ext.init_interval_index, RangeIndexType: bodo.
        hiframes.pd_index_ext.init_range_index}
    if type(I) in rsr__ysvx:
        return rsr__ysvx[type(I)]
    raise BodoError(
        f'Unsupported type for standard Index constructor: {type(I)}')


@overload_method(NumericIndexType, 'min', no_unliteral=True, inline='always')
@overload_method(RangeIndexType, 'min', no_unliteral=True, inline='always')
@overload_method(CategoricalIndexType, 'min', no_unliteral=True, inline=
    'always')
def overload_index_min(I, axis=None, skipna=True):
    grdlp__pza = dict(axis=axis, skipna=skipna)
    bdenf__mso = dict(axis=None, skipna=True)
    check_unsupported_args('Index.min', grdlp__pza, bdenf__mso,
        package_name='pandas', module_name='Index')
    if isinstance(I, RangeIndexType):

        def impl(I, axis=None, skipna=True):
            zyye__mymcx = len(I)
            if zyye__mymcx == 0:
                return np.nan
            if I._step < 0:
                return I._start + I._step * (zyye__mymcx - 1)
            else:
                return I._start
        return impl
    if isinstance(I, CategoricalIndexType):
        if not I.dtype.ordered:
            raise BodoError(
                'Index.min(): only ordered categoricals are possible')

    def impl(I, axis=None, skipna=True):
        owj__szc = bodo.hiframes.pd_index_ext.get_index_data(I)
        return bodo.libs.array_ops.array_op_min(owj__szc)
    return impl


@overload_method(NumericIndexType, 'max', no_unliteral=True, inline='always')
@overload_method(RangeIndexType, 'max', no_unliteral=True, inline='always')
@overload_method(CategoricalIndexType, 'max', no_unliteral=True, inline=
    'always')
def overload_index_max(I, axis=None, skipna=True):
    grdlp__pza = dict(axis=axis, skipna=skipna)
    bdenf__mso = dict(axis=None, skipna=True)
    check_unsupported_args('Index.max', grdlp__pza, bdenf__mso,
        package_name='pandas', module_name='Index')
    if isinstance(I, RangeIndexType):

        def impl(I, axis=None, skipna=True):
            zyye__mymcx = len(I)
            if zyye__mymcx == 0:
                return np.nan
            if I._step > 0:
                return I._start + I._step * (zyye__mymcx - 1)
            else:
                return I._start
        return impl
    if isinstance(I, CategoricalIndexType):
        if not I.dtype.ordered:
            raise BodoError(
                'Index.max(): only ordered categoricals are possible')

    def impl(I, axis=None, skipna=True):
        owj__szc = bodo.hiframes.pd_index_ext.get_index_data(I)
        return bodo.libs.array_ops.array_op_max(owj__szc)
    return impl


@overload_method(NumericIndexType, 'argmin', no_unliteral=True, inline='always'
    )
@overload_method(StringIndexType, 'argmin', no_unliteral=True, inline='always')
@overload_method(BinaryIndexType, 'argmin', no_unliteral=True, inline='always')
@overload_method(DatetimeIndexType, 'argmin', no_unliteral=True, inline=
    'always')
@overload_method(TimedeltaIndexType, 'argmin', no_unliteral=True, inline=
    'always')
@overload_method(CategoricalIndexType, 'argmin', no_unliteral=True, inline=
    'always')
@overload_method(RangeIndexType, 'argmin', no_unliteral=True, inline='always')
@overload_method(PeriodIndexType, 'argmin', no_unliteral=True, inline='always')
def overload_index_argmin(I, axis=0, skipna=True):
    grdlp__pza = dict(axis=axis, skipna=skipna)
    bdenf__mso = dict(axis=0, skipna=True)
    check_unsupported_args('Index.argmin', grdlp__pza, bdenf__mso,
        package_name='pandas', module_name='Index')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(I,
        'Index.argmin()')
    if isinstance(I, RangeIndexType):

        def impl(I, axis=0, skipna=True):
            return (I._step < 0) * (len(I) - 1)
        return impl
    if isinstance(I, CategoricalIndexType) and not I.dtype.ordered:
        raise BodoError(
            'Index.argmin(): only ordered categoricals are possible')

    def impl(I, axis=0, skipna=True):
        owj__szc = bodo.hiframes.pd_index_ext.get_index_data(I)
        index = init_numeric_index(np.arange(len(owj__szc)))
        return bodo.libs.array_ops.array_op_idxmin(owj__szc, index)
    return impl


@overload_method(NumericIndexType, 'argmax', no_unliteral=True, inline='always'
    )
@overload_method(StringIndexType, 'argmax', no_unliteral=True, inline='always')
@overload_method(BinaryIndexType, 'argmax', no_unliteral=True, inline='always')
@overload_method(DatetimeIndexType, 'argmax', no_unliteral=True, inline=
    'always')
@overload_method(TimedeltaIndexType, 'argmax', no_unliteral=True, inline=
    'always')
@overload_method(RangeIndexType, 'argmax', no_unliteral=True, inline='always')
@overload_method(CategoricalIndexType, 'argmax', no_unliteral=True, inline=
    'always')
@overload_method(PeriodIndexType, 'argmax', no_unliteral=True, inline='always')
def overload_index_argmax(I, axis=0, skipna=True):
    grdlp__pza = dict(axis=axis, skipna=skipna)
    bdenf__mso = dict(axis=0, skipna=True)
    check_unsupported_args('Index.argmax', grdlp__pza, bdenf__mso,
        package_name='pandas', module_name='Index')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(I,
        'Index.argmax()')
    if isinstance(I, RangeIndexType):

        def impl(I, axis=0, skipna=True):
            return (I._step > 0) * (len(I) - 1)
        return impl
    if isinstance(I, CategoricalIndexType) and not I.dtype.ordered:
        raise BodoError(
            'Index.argmax(): only ordered categoricals are possible')

    def impl(I, axis=0, skipna=True):
        owj__szc = bodo.hiframes.pd_index_ext.get_index_data(I)
        index = np.arange(len(owj__szc))
        return bodo.libs.array_ops.array_op_idxmax(owj__szc, index)
    return impl


@overload_method(NumericIndexType, 'unique', no_unliteral=True, inline='always'
    )
@overload_method(BinaryIndexType, 'unique', no_unliteral=True, inline='always')
@overload_method(StringIndexType, 'unique', no_unliteral=True, inline='always')
@overload_method(CategoricalIndexType, 'unique', no_unliteral=True, inline=
    'always')
@overload_method(IntervalIndexType, 'unique', no_unliteral=True, inline=
    'always')
@overload_method(DatetimeIndexType, 'unique', no_unliteral=True, inline=
    'always')
@overload_method(TimedeltaIndexType, 'unique', no_unliteral=True, inline=
    'always')
def overload_index_unique(I):
    bds__hywti = get_index_constructor(I)

    def impl(I):
        owj__szc = bodo.hiframes.pd_index_ext.get_index_data(I)
        name = bodo.hiframes.pd_index_ext.get_index_name(I)
        nblg__pxqkw = bodo.libs.array_kernels.unique(owj__szc)
        return bds__hywti(nblg__pxqkw, name)
    return impl


@overload_method(RangeIndexType, 'unique', no_unliteral=True, inline='always')
def overload_range_index_unique(I):

    def impl(I):
        return I.copy()
    return impl


@overload_method(NumericIndexType, 'nunique', inline='always')
@overload_method(BinaryIndexType, 'nunique', inline='always')
@overload_method(StringIndexType, 'nunique', inline='always')
@overload_method(CategoricalIndexType, 'nunique', inline='always')
@overload_method(DatetimeIndexType, 'nunique', inline='always')
@overload_method(TimedeltaIndexType, 'nunique', inline='always')
@overload_method(PeriodIndexType, 'nunique', inline='always')
def overload_index_nunique(I, dropna=True):

    def impl(I, dropna=True):
        owj__szc = bodo.hiframes.pd_index_ext.get_index_data(I)
        syi__wdj = bodo.libs.array_kernels.nunique(owj__szc, dropna)
        return syi__wdj
    return impl


@overload_method(RangeIndexType, 'nunique', inline='always')
def overload_range_index_nunique(I, dropna=True):

    def impl(I, dropna=True):
        start = I._start
        stop = I._stop
        step = I._step
        return max(0, -(-(stop - start) // step))
    return impl


@overload_method(NumericIndexType, 'isin', no_unliteral=True, inline='always')
@overload_method(BinaryIndexType, 'isin', no_unliteral=True, inline='always')
@overload_method(StringIndexType, 'isin', no_unliteral=True, inline='always')
@overload_method(DatetimeIndexType, 'isin', no_unliteral=True, inline='always')
@overload_method(TimedeltaIndexType, 'isin', no_unliteral=True, inline='always'
    )
def overload_index_isin(I, values):
    if bodo.utils.utils.is_array_typ(values):

        def impl_arr(I, values):
            ilfor__ysi = bodo.utils.conversion.coerce_to_array(values)
            A = bodo.hiframes.pd_index_ext.get_index_data(I)
            syi__wdj = len(A)
            qaob__oea = np.empty(syi__wdj, np.bool_)
            bodo.libs.array.array_isin(qaob__oea, A, ilfor__ysi, False)
            return qaob__oea
        return impl_arr
    if not isinstance(values, (types.Set, types.List)):
        raise BodoError(
            "Series.isin(): 'values' parameter should be a set or a list")

    def impl(I, values):
        A = bodo.hiframes.pd_index_ext.get_index_data(I)
        qaob__oea = bodo.libs.array_ops.array_op_isin(A, values)
        return qaob__oea
    return impl


@overload_method(RangeIndexType, 'isin', no_unliteral=True, inline='always')
def overload_range_index_isin(I, values):
    if bodo.utils.utils.is_array_typ(values):

        def impl_arr(I, values):
            ilfor__ysi = bodo.utils.conversion.coerce_to_array(values)
            A = np.arange(I.start, I.stop, I.step)
            syi__wdj = len(A)
            qaob__oea = np.empty(syi__wdj, np.bool_)
            bodo.libs.array.array_isin(qaob__oea, A, ilfor__ysi, False)
            return qaob__oea
        return impl_arr
    if not isinstance(values, (types.Set, types.List)):
        raise BodoError(
            "Index.isin(): 'values' parameter should be a set or a list")

    def impl(I, values):
        A = np.arange(I.start, I.stop, I.step)
        qaob__oea = bodo.libs.array_ops.array_op_isin(A, values)
        return qaob__oea
    return impl


@register_jitable
def order_range(I, ascending):
    step = I._step
    if ascending == (step > 0):
        return I.copy()
    else:
        start = I._start
        stop = I._stop
        name = get_index_name(I)
        zyye__mymcx = len(I)
        dry__fja = start + step * (zyye__mymcx - 1)
        sbl__pock = dry__fja - step * zyye__mymcx
        return init_range_index(dry__fja, sbl__pock, -step, name)


@overload_method(NumericIndexType, 'sort_values', no_unliteral=True, inline
    ='always')
@overload_method(BinaryIndexType, 'sort_values', no_unliteral=True, inline=
    'always')
@overload_method(StringIndexType, 'sort_values', no_unliteral=True, inline=
    'always')
@overload_method(CategoricalIndexType, 'sort_values', no_unliteral=True,
    inline='always')
@overload_method(DatetimeIndexType, 'sort_values', no_unliteral=True,
    inline='always')
@overload_method(TimedeltaIndexType, 'sort_values', no_unliteral=True,
    inline='always')
@overload_method(RangeIndexType, 'sort_values', no_unliteral=True, inline=
    'always')
def overload_index_sort_values(I, return_indexer=False, ascending=True,
    na_position='last', key=None):
    grdlp__pza = dict(return_indexer=return_indexer, key=key)
    bdenf__mso = dict(return_indexer=False, key=None)
    check_unsupported_args('Index.sort_values', grdlp__pza, bdenf__mso,
        package_name='pandas', module_name='Index')
    if not is_overload_bool(ascending):
        raise BodoError(
            "Index.sort_values(): 'ascending' parameter must be of type bool")
    if not is_overload_constant_str(na_position) or get_overload_const_str(
        na_position) not in ('first', 'last'):
        raise_bodo_error(
            "Index.sort_values(): 'na_position' should either be 'first' or 'last'"
            )
    if isinstance(I, RangeIndexType):

        def impl(I, return_indexer=False, ascending=True, na_position=
            'last', key=None):
            return order_range(I, ascending)
        return impl
    bds__hywti = get_index_constructor(I)
    uqfrs__wnm = ColNamesMetaType(('$_bodo_col_',))

    def impl(I, return_indexer=False, ascending=True, na_position='last',
        key=None):
        owj__szc = bodo.hiframes.pd_index_ext.get_index_data(I)
        name = get_index_name(I)
        index = init_range_index(0, len(owj__szc), 1, None)
        evshd__oqe = bodo.hiframes.pd_dataframe_ext.init_dataframe((
            owj__szc,), index, uqfrs__wnm)
        oqd__aekx = evshd__oqe.sort_values(['$_bodo_col_'], ascending=
            ascending, inplace=False, na_position=na_position)
        qaob__oea = bodo.hiframes.pd_dataframe_ext.get_dataframe_data(oqd__aekx
            , 0)
        return bds__hywti(qaob__oea, name)
    return impl


@overload_method(NumericIndexType, 'argsort', no_unliteral=True, inline=
    'always')
@overload_method(BinaryIndexType, 'argsort', no_unliteral=True, inline='always'
    )
@overload_method(StringIndexType, 'argsort', no_unliteral=True, inline='always'
    )
@overload_method(CategoricalIndexType, 'argsort', no_unliteral=True, inline
    ='always')
@overload_method(DatetimeIndexType, 'argsort', no_unliteral=True, inline=
    'always')
@overload_method(TimedeltaIndexType, 'argsort', no_unliteral=True, inline=
    'always')
@overload_method(PeriodIndexType, 'argsort', no_unliteral=True, inline='always'
    )
@overload_method(RangeIndexType, 'argsort', no_unliteral=True, inline='always')
def overload_index_argsort(I, axis=0, kind='quicksort', order=None):
    grdlp__pza = dict(axis=axis, kind=kind, order=order)
    bdenf__mso = dict(axis=0, kind='quicksort', order=None)
    check_unsupported_args('Index.argsort', grdlp__pza, bdenf__mso,
        package_name='pandas', module_name='Index')
    if isinstance(I, RangeIndexType):

        def impl(I, axis=0, kind='quicksort', order=None):
            if I._step > 0:
                return np.arange(0, len(I), 1)
            else:
                return np.arange(len(I) - 1, -1, -1)
        return impl

    def impl(I, axis=0, kind='quicksort', order=None):
        owj__szc = bodo.hiframes.pd_index_ext.get_index_data(I)
        qaob__oea = bodo.hiframes.series_impl.argsort(owj__szc)
        return qaob__oea
    return impl


@overload_method(NumericIndexType, 'where', no_unliteral=True, inline='always')
@overload_method(StringIndexType, 'where', no_unliteral=True, inline='always')
@overload_method(BinaryIndexType, 'where', no_unliteral=True, inline='always')
@overload_method(DatetimeIndexType, 'where', no_unliteral=True, inline='always'
    )
@overload_method(TimedeltaIndexType, 'where', no_unliteral=True, inline=
    'always')
@overload_method(CategoricalIndexType, 'where', no_unliteral=True, inline=
    'always')
@overload_method(RangeIndexType, 'where', no_unliteral=True, inline='always')
def overload_index_where(I, cond, other=np.nan):
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(I,
        'Index.where()')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(other,
        'Index.where()')
    bodo.hiframes.series_impl._validate_arguments_mask_where('where',
        'Index', I, cond, other, inplace=False, axis=None, level=None,
        errors='raise', try_cast=False)
    if is_overload_constant_nan(other):
        havwh__ouk = 'None'
    else:
        havwh__ouk = 'other'
    ncl__uyeu = 'def impl(I, cond, other=np.nan):\n'
    if isinstance(I, RangeIndexType):
        ncl__uyeu += '  arr = np.arange(I._start, I._stop, I._step)\n'
        bds__hywti = 'init_numeric_index'
    else:
        ncl__uyeu += '  arr = bodo.hiframes.pd_index_ext.get_index_data(I)\n'
    ncl__uyeu += '  name = bodo.hiframes.pd_index_ext.get_index_name(I)\n'
    ncl__uyeu += (
        f'  out_arr = bodo.hiframes.series_impl.where_impl(cond, arr, {havwh__ouk})\n'
        )
    ncl__uyeu += f'  return constructor(out_arr, name)\n'
    iqmgk__pwkj = {}
    bds__hywti = init_numeric_index if isinstance(I, RangeIndexType
        ) else get_index_constructor(I)
    exec(ncl__uyeu, {'bodo': bodo, 'np': np, 'constructor': bds__hywti},
        iqmgk__pwkj)
    impl = iqmgk__pwkj['impl']
    return impl


@overload_method(NumericIndexType, 'putmask', no_unliteral=True, inline=
    'always')
@overload_method(StringIndexType, 'putmask', no_unliteral=True, inline='always'
    )
@overload_method(BinaryIndexType, 'putmask', no_unliteral=True, inline='always'
    )
@overload_method(DatetimeIndexType, 'putmask', no_unliteral=True, inline=
    'always')
@overload_method(TimedeltaIndexType, 'putmask', no_unliteral=True, inline=
    'always')
@overload_method(CategoricalIndexType, 'putmask', no_unliteral=True, inline
    ='always')
@overload_method(RangeIndexType, 'putmask', no_unliteral=True, inline='always')
def overload_index_putmask(I, cond, other):
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(I,
        'Index.putmask()')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(other,
        'Index.putmask()')
    bodo.hiframes.series_impl._validate_arguments_mask_where('putmask',
        'Index', I, cond, other, inplace=False, axis=None, level=None,
        errors='raise', try_cast=False)
    if is_overload_constant_nan(other):
        havwh__ouk = 'None'
    else:
        havwh__ouk = 'other'
    ncl__uyeu = 'def impl(I, cond, other):\n'
    ncl__uyeu += '  cond = ~cond\n'
    if isinstance(I, RangeIndexType):
        ncl__uyeu += '  arr = np.arange(I._start, I._stop, I._step)\n'
    else:
        ncl__uyeu += '  arr = bodo.hiframes.pd_index_ext.get_index_data(I)\n'
    ncl__uyeu += '  name = bodo.hiframes.pd_index_ext.get_index_name(I)\n'
    ncl__uyeu += (
        f'  out_arr = bodo.hiframes.series_impl.where_impl(cond, arr, {havwh__ouk})\n'
        )
    ncl__uyeu += f'  return constructor(out_arr, name)\n'
    iqmgk__pwkj = {}
    bds__hywti = init_numeric_index if isinstance(I, RangeIndexType
        ) else get_index_constructor(I)
    exec(ncl__uyeu, {'bodo': bodo, 'np': np, 'constructor': bds__hywti},
        iqmgk__pwkj)
    impl = iqmgk__pwkj['impl']
    return impl


@overload_method(NumericIndexType, 'repeat', no_unliteral=True, inline='always'
    )
@overload_method(StringIndexType, 'repeat', no_unliteral=True, inline='always')
@overload_method(CategoricalIndexType, 'repeat', no_unliteral=True, inline=
    'always')
@overload_method(DatetimeIndexType, 'repeat', no_unliteral=True, inline=
    'always')
@overload_method(TimedeltaIndexType, 'repeat', no_unliteral=True, inline=
    'always')
@overload_method(RangeIndexType, 'repeat', no_unliteral=True, inline='always')
def overload_index_repeat(I, repeats, axis=None):
    grdlp__pza = dict(axis=axis)
    bdenf__mso = dict(axis=None)
    check_unsupported_args('Index.repeat', grdlp__pza, bdenf__mso,
        package_name='pandas', module_name='Index')
    bodo.hiframes.pd_timestamp_ext.check_tz_aware_unsupported(I,
        'Index.repeat()')
    if not (isinstance(repeats, types.Integer) or is_iterable_type(repeats) and
        isinstance(repeats.dtype, types.Integer)):
        raise BodoError(
            "Index.repeat(): 'repeats' should be an integer or array of integers"
            )
    ncl__uyeu = 'def impl(I, repeats, axis=None):\n'
    if not isinstance(repeats, types.Integer):
        ncl__uyeu += (
            '    repeats = bodo.utils.conversion.coerce_to_array(repeats)\n')
    if isinstance(I, RangeIndexType):
        ncl__uyeu += '    arr = np.arange(I._start, I._stop, I._step)\n'
    else:
        ncl__uyeu += '    arr = bodo.hiframes.pd_index_ext.get_index_data(I)\n'
    ncl__uyeu += '    name = bodo.hiframes.pd_index_ext.get_index_name(I)\n'
    ncl__uyeu += (
        '    out_arr = bodo.libs.array_kernels.repeat_kernel(arr, repeats)\n')
    ncl__uyeu += '    return constructor(out_arr, name)'
    iqmgk__pwkj = {}
    bds__hywti = init_numeric_index if isinstance(I, RangeIndexType
        ) else get_index_constructor(I)
    exec(ncl__uyeu, {'bodo': bodo, 'np': np, 'constructor': bds__hywti},
        iqmgk__pwkj)
    impl = iqmgk__pwkj['impl']
    return impl


@overload_method(NumericIndexType, 'is_integer', inline='always')
def overload_is_integer_numeric(I):
    truth = isinstance(I.dtype, types.Integer)
    return lambda I: truth


@overload_method(NumericIndexType, 'is_floating', inline='always')
def overload_is_floating_numeric(I):
    truth = isinstance(I.dtype, types.Float)
    return lambda I: truth


@overload_method(NumericIndexType, 'is_boolean', inline='always')
def overload_is_boolean_numeric(I):
    truth = isinstance(I.dtype, types.Boolean)
    return lambda I: truth


@overload_method(NumericIndexType, 'is_numeric', inline='always')
def overload_is_numeric_numeric(I):
    truth = not isinstance(I.dtype, types.Boolean)
    return lambda I: truth


@overload_method(NumericIndexType, 'is_object', inline='always')
def overload_is_object_numeric(I):
    truth = isinstance(I.dtype, types.Boolean)
    return lambda I: truth


@overload_method(StringIndexType, 'is_object', inline='always')
@overload_method(BinaryIndexType, 'is_object', inline='always')
@overload_method(RangeIndexType, 'is_numeric', inline='always')
@overload_method(RangeIndexType, 'is_integer', inline='always')
@overload_method(CategoricalIndexType, 'is_categorical', inline='always')
@overload_method(IntervalIndexType, 'is_interval', inline='always')
@overload_method(MultiIndexType, 'is_object', inline='always')
def overload_is_methods_true(I):
    return lambda I: True


@overload_method(NumericIndexType, 'is_categorical', inline='always')
@overload_method(NumericIndexType, 'is_interval', inline='always')
@overload_method(StringIndexType, 'is_boolean', inline='always')
@overload_method(StringIndexType, 'is_floating', inline='always')
@overload_method(StringIndexType, 'is_categorical', inline='always')
@overload_method(StringIndexType, 'is_integer', inline='always')
@overload_method(StringIndexType, 'is_interval', inline='always')
@overload_method(StringIndexType, 'is_numeric', inline='always')
@overload_method(BinaryIndexType, 'is_boolean', inline='always')
@overload_method(BinaryIndexType, 'is_floating', inline='always')
@overload_method(BinaryIndexType, 'is_categorical', inline='always')
@overload_method(BinaryIndexType, 'is_integer', inline='always')
@overload_method(BinaryIndexType, 'is_interval', inline='always')
@overload_method(BinaryIndexType, 'is_numeric', inline='always')
@overload_method(DatetimeIndexType, 'is_boolean', inline='always')
@overload_method(DatetimeIndexType, 'is_floating', inline='always')
@overload_method(DatetimeIndexType, 'is_categorical', inline='always')
@overload_method(DatetimeIndexType, 'is_integer', inline='always')
@overload_method(DatetimeIndexType, 'is_interval', inline='always')
@overload_method(DatetimeIndexType, 'is_numeric', inline='always')
@overload_method(DatetimeIndexType, 'is_object', inline='always')
@overload_method(TimedeltaIndexType, 'is_boolean', inline='always')
@overload_method(TimedeltaIndexType, 'is_floating', inline='always')
@overload_method(TimedeltaIndexType, 'is_categorical', inline='always')
@overload_method(TimedeltaIndexType, 'is_integer', inline='always')
@overload_method(TimedeltaIndexType, 'is_interval', inline='always')
@overload_method(TimedeltaIndexType, 'is_numeric', inline='always')
@overload_method(TimedeltaIndexType, 'is_object', inline='always')
@overload_method(RangeIndexType, 'is_boolean', inline='always')
@overload_method(RangeIndexType, 'is_floating', inline='always')
@overload_method(RangeIndexType, 'is_categorical', inline='always')
@overload_method(RangeIndexType, 'is_interval', inline='always')
@overload_method(RangeIndexType, 'is_object', inline='always')
@overload_method(IntervalIndexType, 'is_boolean', inline='always')
@overload_method(IntervalIndexType, 'is_floating', inline='always')
@overload_method(IntervalIndexType, 'is_categorical', inline='always')
@overload_method(IntervalIndexType, 'is_integer', inline='always')
@overload_method(IntervalIndexType, 'is_numeric', inline='always')
@overload_method(IntervalIndexType, 'is_object', inline='always')
@overload_method(CategoricalIndexType, 'is_boolean', inline='always')
@overload_method(CategoricalIndexType, 'is_floating', inline='always')
@overload_method(CategoricalIndexType, 'is_integer', inline='always')
@overload_method(CategoricalIndexType, 'is_interval', inline='always')
@overload_method(CategoricalIndexType, 'is_numeric', inline='always')
@overload_method(CategoricalIndexType, 'is_object', inline='always')
@overload_method(PeriodIndexType, 'is_boolean', inline='always')
@overload_method(PeriodIndexType, 'is_floating', inline='always')
@overload_method(PeriodIndexType, 'is_categorical', inline='always')
@overload_method(PeriodIndexType, 'is_integer', inline='always')
@overload_method(PeriodIndexType, 'is_interval', inline='always')
@overload_method(PeriodIndexType, 'is_numeric', inline='always')
@overload_method(PeriodIndexType, 'is_object', inline='always')
@overload_method(MultiIndexType, 'is_boolean', inline='always')
@overload_method(MultiIndexType, 'is_floating', inline='always')
@overload_method(MultiIndexType, 'is_categorical', inline='always')
@overload_method(MultiIndexType, 'is_integer', inline='always')
@overload_method(MultiIndexType, 'is_interval', inline='always')
@overload_method(MultiIndexType, 'is_numeric', inline='always')
def overload_is_methods_false(I):
    return lambda I: False


@overload(operator.getitem, no_unliteral=True)
def overload_heter_index_getitem(I, ind):
    if not isinstance(I, HeterogeneousIndexType):
        return
    if isinstance(ind, types.Integer):
        return lambda I, ind: bodo.hiframes.pd_index_ext.get_index_data(I)[ind]
    if isinstance(I, HeterogeneousIndexType):
        return lambda I, ind: bodo.hiframes.pd_index_ext.init_heter_index(bodo
            .hiframes.pd_index_ext.get_index_data(I)[ind], bodo.hiframes.
            pd_index_ext.get_index_name(I))


@lower_constant(DatetimeIndexType)
@lower_constant(TimedeltaIndexType)
def lower_constant_time_index(context, builder, ty, pyval):
    if isinstance(ty.data, bodo.DatetimeArrayType):
        data = context.get_constant_generic(builder, ty.data, pyval.array)
    else:
        data = context.get_constant_generic(builder, types.Array(types.
            int64, 1, 'C'), pyval.values.view(np.int64))
    name = context.get_constant_generic(builder, ty.name_typ, pyval.name)
    dtype = ty.dtype
    caade__ysmi = context.get_constant_null(types.DictType(dtype, types.int64))
    return lir.Constant.literal_struct([data, name, caade__ysmi])


@lower_constant(PeriodIndexType)
def lower_constant_period_index(context, builder, ty, pyval):
    data = context.get_constant_generic(builder, bodo.IntegerArrayType(
        types.int64), pd.arrays.IntegerArray(pyval.asi8, pyval.isna()))
    name = context.get_constant_generic(builder, ty.name_typ, pyval.name)
    caade__ysmi = context.get_constant_null(types.DictType(types.int64,
        types.int64))
    return lir.Constant.literal_struct([data, name, caade__ysmi])


@lower_constant(NumericIndexType)
def lower_constant_numeric_index(context, builder, ty, pyval):
    assert isinstance(ty.dtype, (types.Integer, types.Float, types.Boolean))
    data = context.get_constant_generic(builder, types.Array(ty.dtype, 1,
        'C'), pyval.values)
    name = context.get_constant_generic(builder, ty.name_typ, pyval.name)
    dtype = ty.dtype
    caade__ysmi = context.get_constant_null(types.DictType(dtype, types.int64))
    return lir.Constant.literal_struct([data, name, caade__ysmi])


@lower_constant(StringIndexType)
@lower_constant(BinaryIndexType)
def lower_constant_binary_string_index(context, builder, ty, pyval):
    gps__gxxcf = ty.data
    scalar_type = ty.data.dtype
    data = context.get_constant_generic(builder, gps__gxxcf, pyval.values)
    name = context.get_constant_generic(builder, ty.name_typ, pyval.name)
    caade__ysmi = context.get_constant_null(types.DictType(scalar_type,
        types.int64))
    return lir.Constant.literal_struct([data, name, caade__ysmi])


@lower_builtin('getiter', RangeIndexType)
def getiter_range_index(context, builder, sig, args):
    [cfi__utqsf] = sig.args
    [index] = args
    opgr__yae = context.make_helper(builder, cfi__utqsf, value=index)
    phiat__kfp = context.make_helper(builder, sig.return_type)
    eznqs__xxwa = cgutils.alloca_once_value(builder, opgr__yae.start)
    duodw__tlzit = context.get_constant(types.intp, 0)
    pnx__kal = cgutils.alloca_once_value(builder, duodw__tlzit)
    phiat__kfp.iter = eznqs__xxwa
    phiat__kfp.stop = opgr__yae.stop
    phiat__kfp.step = opgr__yae.step
    phiat__kfp.count = pnx__kal
    dmwp__jjz = builder.sub(opgr__yae.stop, opgr__yae.start)
    ajp__gmxl = context.get_constant(types.intp, 1)
    xkxw__bwjd = builder.icmp_signed('>', dmwp__jjz, duodw__tlzit)
    curul__ctn = builder.icmp_signed('>', opgr__yae.step, duodw__tlzit)
    uxo__zdqo = builder.not_(builder.xor(xkxw__bwjd, curul__ctn))
    with builder.if_then(uxo__zdqo):
        jqw__htnx = builder.srem(dmwp__jjz, opgr__yae.step)
        jqw__htnx = builder.select(xkxw__bwjd, jqw__htnx, builder.neg(
            jqw__htnx))
        bays__elac = builder.icmp_signed('>', jqw__htnx, duodw__tlzit)
        afag__fcxp = builder.add(builder.sdiv(dmwp__jjz, opgr__yae.step),
            builder.select(bays__elac, ajp__gmxl, duodw__tlzit))
        builder.store(afag__fcxp, pnx__kal)
    plegg__ikob = phiat__kfp._getvalue()
    vbv__txbvb = impl_ret_new_ref(context, builder, sig.return_type,
        plegg__ikob)
    return vbv__txbvb


def _install_index_getiter():
    index_types = [NumericIndexType, StringIndexType, BinaryIndexType,
        CategoricalIndexType, TimedeltaIndexType, DatetimeIndexType]
    for typ in index_types:
        lower_builtin('getiter', typ)(numba.np.arrayobj.getiter_array)


_install_index_getiter()
index_unsupported_methods = ['append', 'asof', 'asof_locs', 'astype',
    'delete', 'drop', 'droplevel', 'dropna', 'equals', 'factorize',
    'fillna', 'format', 'get_indexer', 'get_indexer_for',
    'get_indexer_non_unique', 'get_level_values', 'get_slice_bound',
    'get_value', 'groupby', 'holds_integer', 'identical', 'insert', 'is_',
    'is_mixed', 'is_type_compatible', 'item', 'join', 'memory_usage',
    'ravel', 'reindex', 'searchsorted', 'set_names', 'set_value', 'shift',
    'slice_indexer', 'slice_locs', 'sort', 'sortlevel', 'str',
    'to_flat_index', 'to_native_types', 'transpose', 'value_counts', 'view']
index_unsupported_atrs = ['array', 'asi8', 'has_duplicates', 'hasnans',
    'is_unique']
cat_idx_unsupported_atrs = ['codes', 'categories', 'ordered',
    'is_monotonic', 'is_monotonic_increasing', 'is_monotonic_decreasing']
cat_idx_unsupported_methods = ['rename_categories', 'reorder_categories',
    'add_categories', 'remove_categories', 'remove_unused_categories',
    'set_categories', 'as_ordered', 'as_unordered', 'get_loc', 'isin',
    'all', 'any', 'union', 'intersection', 'difference', 'symmetric_difference'
    ]
interval_idx_unsupported_atrs = ['closed', 'is_empty',
    'is_non_overlapping_monotonic', 'is_overlapping', 'left', 'right',
    'mid', 'length', 'values', 'nbytes', 'is_monotonic',
    'is_monotonic_increasing', 'is_monotonic_decreasing', 'dtype']
interval_idx_unsupported_methods = ['contains', 'copy', 'overlaps',
    'set_closed', 'to_tuples', 'take', 'get_loc', 'isna', 'isnull', 'map',
    'isin', 'all', 'any', 'argsort', 'sort_values', 'argmax', 'argmin',
    'where', 'putmask', 'nunique', 'union', 'intersection', 'difference',
    'symmetric_difference', 'to_series', 'to_frame', 'to_list', 'tolist',
    'repeat', 'min', 'max']
multi_index_unsupported_atrs = ['levshape', 'levels', 'codes', 'dtypes',
    'values', 'is_monotonic', 'is_monotonic_increasing',
    'is_monotonic_decreasing']
multi_index_unsupported_methods = ['copy', 'set_levels', 'set_codes',
    'swaplevel', 'reorder_levels', 'remove_unused_levels', 'get_loc',
    'get_locs', 'get_loc_level', 'take', 'isna', 'isnull', 'map', 'isin',
    'unique', 'all', 'any', 'argsort', 'sort_values', 'argmax', 'argmin',
    'where', 'putmask', 'nunique', 'union', 'intersection', 'difference',
    'symmetric_difference', 'to_series', 'to_list', 'tolist', 'to_numpy',
    'repeat', 'min', 'max']
dt_index_unsupported_atrs = ['time', 'timez', 'tz', 'freq', 'freqstr',
    'inferred_freq']
dt_index_unsupported_methods = ['normalize', 'strftime', 'snap',
    'tz_localize', 'round', 'floor', 'ceil', 'to_period', 'to_perioddelta',
    'to_pydatetime', 'month_name', 'day_name', 'mean', 'indexer_at_time',
    'indexer_between', 'indexer_between_time', 'all', 'any']
td_index_unsupported_atrs = ['components', 'inferred_freq']
td_index_unsupported_methods = ['to_pydatetime', 'round', 'floor', 'ceil',
    'mean', 'all', 'any']
period_index_unsupported_atrs = ['day', 'dayofweek', 'day_of_week',
    'dayofyear', 'day_of_year', 'days_in_month', 'daysinmonth', 'freq',
    'freqstr', 'hour', 'is_leap_year', 'minute', 'month', 'quarter',
    'second', 'week', 'weekday', 'weekofyear', 'year', 'end_time', 'qyear',
    'start_time', 'is_monotonic', 'is_monotonic_increasing',
    'is_monotonic_decreasing', 'dtype']
period_index_unsupported_methods = ['asfreq', 'strftime', 'to_timestamp',
    'isin', 'unique', 'all', 'any', 'where', 'putmask', 'sort_values',
    'union', 'intersection', 'difference', 'symmetric_difference',
    'to_series', 'to_frame', 'to_numpy', 'to_list', 'tolist', 'repeat',
    'min', 'max']
string_index_unsupported_atrs = ['is_monotonic', 'is_monotonic_increasing',
    'is_monotonic_decreasing']
string_index_unsupported_methods = ['min', 'max']
binary_index_unsupported_atrs = ['is_monotonic', 'is_monotonic_increasing',
    'is_monotonic_decreasing']
binary_index_unsupported_methods = ['repeat', 'min', 'max']
index_types = [('pandas.RangeIndex.{}', RangeIndexType), (
    'pandas.Index.{} with numeric data', NumericIndexType), (
    'pandas.Index.{} with string data', StringIndexType), (
    'pandas.Index.{} with binary data', BinaryIndexType), (
    'pandas.TimedeltaIndex.{}', TimedeltaIndexType), (
    'pandas.IntervalIndex.{}', IntervalIndexType), (
    'pandas.CategoricalIndex.{}', CategoricalIndexType), (
    'pandas.PeriodIndex.{}', PeriodIndexType), ('pandas.DatetimeIndex.{}',
    DatetimeIndexType), ('pandas.MultiIndex.{}', MultiIndexType)]
for name, typ in index_types:
    idx_typ_to_format_str_map[typ] = name


def _install_index_unsupported():
    for crl__keit in index_unsupported_methods:
        for fxsll__mfq, typ in index_types:
            overload_method(typ, crl__keit, no_unliteral=True)(
                create_unsupported_overload(fxsll__mfq.format(crl__keit +
                '()')))
    for mcb__kuw in index_unsupported_atrs:
        for fxsll__mfq, typ in index_types:
            overload_attribute(typ, mcb__kuw, no_unliteral=True)(
                create_unsupported_overload(fxsll__mfq.format(mcb__kuw)))
    gbf__nvnru = [(StringIndexType, string_index_unsupported_atrs), (
        BinaryIndexType, binary_index_unsupported_atrs), (
        CategoricalIndexType, cat_idx_unsupported_atrs), (IntervalIndexType,
        interval_idx_unsupported_atrs), (MultiIndexType,
        multi_index_unsupported_atrs), (DatetimeIndexType,
        dt_index_unsupported_atrs), (TimedeltaIndexType,
        td_index_unsupported_atrs), (PeriodIndexType,
        period_index_unsupported_atrs)]
    kpd__buaq = [(CategoricalIndexType, cat_idx_unsupported_methods), (
        IntervalIndexType, interval_idx_unsupported_methods), (
        MultiIndexType, multi_index_unsupported_methods), (
        DatetimeIndexType, dt_index_unsupported_methods), (
        TimedeltaIndexType, td_index_unsupported_methods), (PeriodIndexType,
        period_index_unsupported_methods), (BinaryIndexType,
        binary_index_unsupported_methods), (StringIndexType,
        string_index_unsupported_methods)]
    for typ, nnpuh__teu in kpd__buaq:
        fxsll__mfq = idx_typ_to_format_str_map[typ]
        for loa__totmy in nnpuh__teu:
            overload_method(typ, loa__totmy, no_unliteral=True)(
                create_unsupported_overload(fxsll__mfq.format(loa__totmy +
                '()')))
    for typ, ftuhs__bmy in gbf__nvnru:
        fxsll__mfq = idx_typ_to_format_str_map[typ]
        for mcb__kuw in ftuhs__bmy:
            overload_attribute(typ, mcb__kuw, no_unliteral=True)(
                create_unsupported_overload(fxsll__mfq.format(mcb__kuw)))


_install_index_unsupported()
