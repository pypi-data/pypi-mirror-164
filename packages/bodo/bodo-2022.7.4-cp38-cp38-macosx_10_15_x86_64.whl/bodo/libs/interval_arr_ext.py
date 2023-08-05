"""
Array of intervals corresponding to IntervalArray of Pandas.
Used for IntervalIndex, which is necessary for Series.value_counts() with 'bins'
argument.
"""
import numba
import pandas as pd
from numba.core import cgutils, types
from numba.extending import NativeValue, box, intrinsic, make_attribute_wrapper, models, overload, overload_attribute, overload_method, register_model, typeof_impl, unbox
from numba.parfors.array_analysis import ArrayAnalysis
import bodo


class IntervalType(types.Type):

    def __init__(self):
        super(IntervalType, self).__init__('IntervalType()')


class IntervalArrayType(types.ArrayCompatible):

    def __init__(self, arr_type):
        self.arr_type = arr_type
        self.dtype = IntervalType()
        super(IntervalArrayType, self).__init__(name=
            f'IntervalArrayType({arr_type})')

    @property
    def as_array(self):
        return types.Array(types.undefined, 1, 'C')

    def copy(self):
        return IntervalArrayType(self.arr_type)

    @property
    def mangling_args(self):
        return self.__class__.__name__, (self._code,)


@register_model(IntervalArrayType)
class IntervalArrayModel(models.StructModel):

    def __init__(self, dmm, fe_type):
        tozy__ucyyi = [('left', fe_type.arr_type), ('right', fe_type.arr_type)]
        models.StructModel.__init__(self, dmm, fe_type, tozy__ucyyi)


make_attribute_wrapper(IntervalArrayType, 'left', '_left')
make_attribute_wrapper(IntervalArrayType, 'right', '_right')


@typeof_impl.register(pd.arrays.IntervalArray)
def typeof_interval_array(val, c):
    arr_type = bodo.typeof(val._left)
    return IntervalArrayType(arr_type)


@intrinsic
def init_interval_array(typingctx, left, right=None):
    assert left == right, 'Interval left/right array types should be the same'

    def codegen(context, builder, signature, args):
        rtagm__isv, kprxc__tjvbp = args
        vvv__shrh = cgutils.create_struct_proxy(signature.return_type)(context,
            builder)
        vvv__shrh.left = rtagm__isv
        vvv__shrh.right = kprxc__tjvbp
        context.nrt.incref(builder, signature.args[0], rtagm__isv)
        context.nrt.incref(builder, signature.args[1], kprxc__tjvbp)
        return vvv__shrh._getvalue()
    bva__mfj = IntervalArrayType(left)
    arfz__mwpgp = bva__mfj(left, right)
    return arfz__mwpgp, codegen


def init_interval_array_equiv(self, scope, equiv_set, loc, args, kws):
    assert len(args) == 2 and not kws
    cghu__wuhz = []
    for ziuth__uhlg in args:
        cpsi__ywsmt = equiv_set.get_shape(ziuth__uhlg)
        if cpsi__ywsmt is not None:
            cghu__wuhz.append(cpsi__ywsmt[0])
    if len(cghu__wuhz) > 1:
        equiv_set.insert_equiv(*cghu__wuhz)
    left = args[0]
    if equiv_set.has_shape(left):
        return ArrayAnalysis.AnalyzeResult(shape=left, pre=[])
    return None


(ArrayAnalysis._analyze_op_call_bodo_libs_interval_arr_ext_init_interval_array
    ) = init_interval_array_equiv


def alias_ext_init_interval_array(lhs_name, args, alias_map, arg_aliases):
    assert len(args) == 2
    numba.core.ir_utils._add_alias(lhs_name, args[0].name, alias_map,
        arg_aliases)
    numba.core.ir_utils._add_alias(lhs_name, args[1].name, alias_map,
        arg_aliases)


numba.core.ir_utils.alias_func_extensions['init_interval_array',
    'bodo.libs.int_arr_ext'] = alias_ext_init_interval_array


@box(IntervalArrayType)
def box_interval_arr(typ, val, c):
    vvv__shrh = cgutils.create_struct_proxy(typ)(c.context, c.builder, val)
    c.context.nrt.incref(c.builder, typ.arr_type, vvv__shrh.left)
    ytcis__vmmu = c.pyapi.from_native_value(typ.arr_type, vvv__shrh.left, c
        .env_manager)
    c.context.nrt.incref(c.builder, typ.arr_type, vvv__shrh.right)
    vol__luy = c.pyapi.from_native_value(typ.arr_type, vvv__shrh.right, c.
        env_manager)
    nrk__qbhso = c.context.insert_const_string(c.builder.module, 'pandas')
    uohm__qalho = c.pyapi.import_module_noblock(nrk__qbhso)
    vxtrc__rti = c.pyapi.object_getattr_string(uohm__qalho, 'arrays')
    vhpk__vxvm = c.pyapi.object_getattr_string(vxtrc__rti, 'IntervalArray')
    pwzr__vnsuv = c.pyapi.call_method(vhpk__vxvm, 'from_arrays', (
        ytcis__vmmu, vol__luy))
    c.pyapi.decref(ytcis__vmmu)
    c.pyapi.decref(vol__luy)
    c.pyapi.decref(uohm__qalho)
    c.pyapi.decref(vxtrc__rti)
    c.pyapi.decref(vhpk__vxvm)
    c.context.nrt.decref(c.builder, typ, val)
    return pwzr__vnsuv


@unbox(IntervalArrayType)
def unbox_interval_arr(typ, val, c):
    ytcis__vmmu = c.pyapi.object_getattr_string(val, '_left')
    left = c.pyapi.to_native_value(typ.arr_type, ytcis__vmmu).value
    c.pyapi.decref(ytcis__vmmu)
    vol__luy = c.pyapi.object_getattr_string(val, '_right')
    right = c.pyapi.to_native_value(typ.arr_type, vol__luy).value
    c.pyapi.decref(vol__luy)
    vvv__shrh = cgutils.create_struct_proxy(typ)(c.context, c.builder)
    vvv__shrh.left = left
    vvv__shrh.right = right
    ujvfs__gogb = cgutils.is_not_null(c.builder, c.pyapi.err_occurred())
    return NativeValue(vvv__shrh._getvalue(), is_error=ujvfs__gogb)


@overload(len, no_unliteral=True)
def overload_interval_arr_len(A):
    if isinstance(A, IntervalArrayType):
        return lambda A: len(A._left)


@overload_attribute(IntervalArrayType, 'shape')
def overload_interval_arr_shape(A):
    return lambda A: (len(A._left),)


@overload_attribute(IntervalArrayType, 'ndim')
def overload_interval_arr_ndim(A):
    return lambda A: 1


@overload_attribute(IntervalArrayType, 'nbytes')
def overload_interval_arr_nbytes(A):
    return lambda A: A._left.nbytes + A._right.nbytes


@overload_method(IntervalArrayType, 'copy', no_unliteral=True)
def overload_interval_arr_copy(A):
    return lambda A: bodo.libs.interval_arr_ext.init_interval_array(A._left
        .copy(), A._right.copy())
