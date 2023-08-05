import hashlib
import inspect
import warnings
import pandas as pd
pandas_version = tuple(map(int, pd.__version__.split('.')[:2]))
_check_pandas_change = False
if pandas_version < (1, 4):

    def _set_noconvert_columns(self):
        assert self.orig_names is not None
        qanon__unrxj = {ibrt__bqo: csqg__rctfg for csqg__rctfg, ibrt__bqo in
            enumerate(self.orig_names)}
        phes__yhroc = [qanon__unrxj[ibrt__bqo] for ibrt__bqo in self.names]
        kjki__aki = self._set_noconvert_dtype_columns(phes__yhroc, self.names)
        for kgo__ycdln in kjki__aki:
            self._reader.set_noconvert(kgo__ycdln)
    if _check_pandas_change:
        lines = inspect.getsource(pd.io.parsers.c_parser_wrapper.
            CParserWrapper._set_noconvert_columns)
        if (hashlib.sha256(lines.encode()).hexdigest() !=
            'afc2d738f194e3976cf05d61cb16dc4224b0139451f08a1cf49c578af6f975d3'
            ):
            warnings.warn(
                'pd.io.parsers.c_parser_wrapper.CParserWrapper._set_noconvert_columns has changed'
                )
    (pd.io.parsers.c_parser_wrapper.CParserWrapper._set_noconvert_columns
        ) = _set_noconvert_columns
