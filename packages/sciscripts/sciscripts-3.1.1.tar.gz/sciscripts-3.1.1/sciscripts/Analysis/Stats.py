#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: T. Malfatti <malfatti@disroot.org>
@date: 20170612
@license: GNU GPLv3 <https://gitlab.com/malfatti/SciScripts/raw/master/LICENSE>
@homepage: https://gitlab.com/Malfatti/SciScripts
"""

ScriptName = 'Analysis.Stats'
print(f'[{ScriptName}] Loading dependencies...')
import inspect, numpy as np
from itertools import combinations, product
from scipy import stats as sst
from scipy.special import btdtr
from statsmodels.stats.multitest import multipletests

from sciscripts.IO.Txt import Print
from sciscripts.IO.Bin import MergeDictsAndContents


try:
    from unidip import UniDip
    from unidip.dip import diptst
    Availunidip = True
except ModuleNotFoundError as e:
    print(f'[{ScriptName}] {e}: Module `unidip` not available. Some functions will not work.')
    Availunidip = False

try:
    # Silence R callback
    import rpy2.rinterface_lib.callbacks
    rpy2.rinterface_lib.callbacks.consolewrite_warnerror = lambda *args: None
    rpy2.rinterface_lib.callbacks.consolewrite_print = lambda *args: None

    from rpy2 import robjects as RObj
    from rpy2.robjects import packages as RPkg
except ModuleNotFoundError as e:
    print(f'[{ScriptName}] {e}: Module `rpy2` not available. Some functions will not work.')

print(f'[{ScriptName}] Done.')

SubAnovas = ('ANOVA','WelchAnOVa','KruskalWallis','Friedman')
SubPWCs = ('TTest', 'Wilcoxon', 'MannWhitneyU')

## Level 0
def _pyKruskalWallis(Data, Factor, FactorName='Factor', FactorsGroupBy=[], FactorGBNames=[], pAdj='holm'):
    if not len(FactorGBNames):
        FactorGBNames = [f'FactorGB{_+1}' for _ in range(len(FactorsGroupBy))]

    Test = {}
    FLs = np.unique(Factor)
    sf = sst.kruskal
    sfa = {'nan_policy':'omit'}

    if len(FactorsGroupBy):
        Test = {**Test, **{_:[] for _ in FactorGBNames}}
        Test = {**Test, **{_:[] for _ in ('n','statistic','p')}}
        FacPr = tuple(product(*[np.unique(_) for _ in FactorsGroupBy]))

        for FC in FacPr:
            i = np.prod([FactorsGroupBy[l]==L for l,L in enumerate(FC)], axis=0, dtype=bool)
            iFLs = np.unique(Factor[i])
            s, p = sf(*[Data[i*(Factor==l)] for l in iFLs], **sfa)

            Test['n'].append(Data[i].shape[0])
            Test['statistic'].append(s)
            Test['p'].append(p)

            for fn,FN in enumerate(FactorGBNames): Test[FN].append(FC[fn])

        Test = {k:np.array(v) for k,v in Test.items()}
        Test['p.adj'] = multipletests(Test['p'], method=pAdj)[1]

    else:
        sp = np.array(sf(*[Data[Factor==l] for l in FLs], **sfa))
        Test['n'] = np.array([Data.shape[0]])
        Test['statistic'] = sp[:1]
        Test['p'] = sp[1:]
        Test['p.adj'] = sp[1:]

    Test['Effect'] = np.repeat([FactorName], len(Test['p']))
    Test['df'] = np.repeat([len(FLs)], len(Test['p']))

    Result = {'KruskalWallis': Test}

    return(Result)


def _KendallsW(Data, Factor):
    FLs = np.unique(Factor)
    if len(FLs) < 3:
        raise ValueError("The number of levels in `Factor` must be >2.")

    N = [Data[Factor==_].shape[0] for _ in FLs]
    if len(np.unique(N)) > 1:
        raise ValueError("The number of data points must match between levels of `Factor`.")
    N = N[0]

    Sums = [Data[Factor==_].sum() for _ in FLs]
    RankSumMean = sum(Sums)/len(FLs)
    SqSum = sum([(_ - RankSumMean)**2 for _ in Sums])
    W = (12*SqSum)/(N**2 * (len(FLs)**3 - len(FLs)))

    return(W)


def dfTTest(a, b, Paired, EqualVar):
    if Paired:
        df = a.shape[0]-1
    else:
        n1 = a.shape[0]
        n2 = b.shape[0]
        v1 = np.var(a, 0, ddof=1)
        v2 = np.var(b, 0, ddof=1)

        if EqualVar:
            df, _ = sst._equal_var_ttest_denom(v1, n1, v2, n2)
        else:
            df, _ = sst._unequal_var_ttest_denom(v1, n1, v2, n2)

    return(df)


def FreedmanDiaconis(Signal, IQR=(25, 75)):
    SignalIQR = sst.iqr(Signal, rng=IQR)
    BinWidth = (2 * SignalIQR)/(Signal.shape[0]**(1/3))
    BinSize = np.ptp(Signal)/BinWidth
    return(BinSize, BinWidth)


def GetSigEff(Anova):
    pss = Anova['p']<0.05
    if True in pss:
        pssFacOrder = sorted(
            [_.split(':') for _ in Anova['Effect'][pss]],
            key=lambda x:len(x), reverse=True
        )
        pssFacOrder = [sorted(pssFacOrder[0])]+[
            sorted(p) if len(p)>1 else p for p in pssFacOrder[1:]
            # if not np.prod([_ in pssFacOrder[0] for _ in ['Epoch', 'Class']])
        ]
    else:
        pssFacOrder = []

    return(pssFacOrder)


def IsMatched(Factor, Paired, FactorsGroupBy=[]):
    ThisFactor = np.array(Factor)
    if ThisFactor.dtype == np.dtype('O'):
        raise TypeError('`Factor` should be a list or array of strings!')

    if Paired:
        if len(FactorsGroupBy):
            IM = [[f==fac for fac in np.unique(f)] for f in FactorsGroupBy]
            IM = [
                np.prod(
                    [IM[e][el] for e,el in enumerate(p)]
                    , axis=0
                ).astype(bool)
                for p in product(*(range(len(_)) for _ in IM))
            ]

            IM = [
                np.unique([
                    ThisFactor[i*(ThisFactor==_)].shape
                    for _ in np.unique(ThisFactor)
                ]).shape[0] == 1
                for i in IM
            ]

            IM = False not in IM
        else:
            IM = [len(ThisFactor[ThisFactor==_]) for _ in np.unique(ThisFactor)]
            IM = np.unique(IM).shape[0] == 1
    else:
        IM = False


    return(IM)


def OrderKeys(Dict, FactorNames):
    Keys = list(Dict.keys())
    Order = sorted([_ for _ in Keys if _ in FactorNames])
    Order += [_ for _ in Keys if _ == 'Effect']
    Order += sorted([_ for _ in Keys if 'group' in _])
    Order += sorted([_ for _ in Keys if _ in ('n','n1','n2')])
    Order += sorted([_ for _ in Keys if 'mean' in _ or 'std' in _ or 'sem' in _ or 'var' in _])
    Order += sorted([_ for _ in Keys if _ not in Order])
    return(Order)


def PairwiseDescribe(Data, Factor, FactorsGroupBy=[], FactorGBNames=[]):
    if not len(FactorGBNames):
        FactorGBNames = [f'FactorGB{_+1}' for _ in range(len(FactorsGroupBy))]

    Test = {}
    if type(Factor) == str:
        Test = {_:[] for _ in FactorGBNames}
        Test = {**Test, **{_:[] for _ in ('n','mean','std','var')}}
        if len(FactorsGroupBy):
            FacPr = tuple(product(*[np.unique(_) for _ in FactorsGroupBy]))
            for FC in FacPr:
                i = np.prod([FactorsGroupBy[l]==L for l,L in enumerate(FC)], axis=0, dtype=bool)
                Test['n'].append(Data[i].shape[0])
                Test['mean'].append(np.nanmean(Data[i]))
                Test['std'].append(np.nanstd(Data[i]))
                Test['var'].append(np.var(Data[i], ddof=1))

                for fn,FN in enumerate(FactorGBNames): Test[FN].append(FC[fn])
        else:
            Test['n'].append(Data.shape[0])
            Test['mean'].append(np.nanmean(Data))
            Test['std'].append(np.nanstd(Data))
            Test['var'].append(np.var(Data, ddof=1))

        Test = {k:np.array(v) for k,v in Test.items()}
        Test['sem'] = Test['std']/(Test['n']**0.5)

    else:
        FLs = np.unique(Factor)
        if len(FLs) != 2:
            raise ValueError('The number of levels in `Factor` must be 2.')

        if len(FactorsGroupBy):
            Test = {**Test, **{_:[] for _ in FactorGBNames}}
            Test = {**Test, **{_:[] for _ in (
                'group1', 'group2', 'n1', 'n2', 'mean1', 'mean2',
                'std1', 'std2', 'var1', 'var2'
            )}}
            FacPr = tuple(product(*[np.unique(_) for _ in FactorsGroupBy]))

            for FC in FacPr:
                i = np.prod([FactorsGroupBy[l]==L for l,L in enumerate(FC)], axis=0, dtype=bool)

                for L,FL in enumerate(FLs):
                    Test[f'group{L+1}'].append(FL)
                    Test[f'n{L+1}'].append(Data[i*(Factor==FL)].shape[0])
                    Test[f'mean{L+1}'].append(np.nanmean(Data[i*(Factor==FL)]))
                    Test[f'std{L+1}'].append(np.nanstd(Data[i*(Factor==FL)]))
                    Test[f'var{L+1}'].append(np.nanvar(Data[i*(Factor==FL)], ddof=1))

                for fn,FN in enumerate(FactorGBNames): Test[FN].append(FC[fn])

            Test = {k:np.array(v) for k,v in Test.items()}

        else:
            for L,FL in enumerate(FLs):
                Test[f'group{L+1}'] = np.array([FL])
                Test[f'n{L+1}'] = np.array([Data[Factor==FL].shape[0]])
                Test[f'mean{L+1}'] = np.array([np.nanmean(Data[Factor==FL])])
                Test[f'std{L+1}'] = np.array([np.nanstd(Data[Factor==FL])])
                Test[f'var{L+1}'] = np.array([np.nanvar(Data[Factor==FL], ddof=1)])

        for FL in ('1','2'):
            Test[f'sem{FL}'] = Test[f'std{FL}']/(Test[f'n{FL}']**0.5)

    Test = {K: Test[K] for K in sorted(Test.keys())}

    return(Test)


def PearsonRP(A,B):
    r = sst.pearsonr(A, B)
    r = list(r)
    r[0] = round(r[0], 3)
    if r[1] < 0.05:
        r[1] = '%.1e' % r[1] + ' *'
    else:
        r[1] = str(round(r[1], 3))

    return(r)


def PearsonRP2D(Data, Mode='Bottom', Alt='two.sided'):
    # # Slow, stable mode:
    # n = Data.shape[1]
    # r = np.ones((n, n), dtype=float)
    # p = np.ones((n, n), dtype=float)

    # for L in range(n):
    #     for C in range(n):
    #         if L == C:
    #             LCr, LCp = (1,0)
    #         else:
    #             if Mode.lower() == 'bottom' and L < C:
    #                 LCr, LCp = [np.nan]*2
    #             elif Mode.lower() == 'upper' and L > C:
    #                 LCr, LCp = [np.nan]*2
    #             else:
    #                 LCr, LCp = sst.pearsonr(Data[:,L], Data[:,C])

    #         r[L,C], p[L,C] = LCr, LCp

    # Faster, may break in the future because of btdtr
    n, Cols = Data.shape
    r = np.corrcoef(Data.T)
    if Mode.lower() == 'bottom':
        for l in range(r.shape[0]): r[l,l+1:] = np.nan
    elif Mode.lower() == 'upper':
        for l in range(r.shape[0]): r[l,:l+1] = np.nan

    # Taken from scipy.stats.pearsonr
    ab = n/2 - 1
    alternative = Alt.replace('.','-')
    if alternative == 'two-sided':
        p = 2*btdtr(ab, ab, 0.5*(1 - abs(np.float64(r))))
    elif alternative == 'less':
        p = 1 - btdtr(ab, ab, 0.5*(1 - abs(np.float64(r))))
    elif alternative == 'greater':
        p = btdtr(ab, ab, 0.5*(1 - abs(np.float64(r))))
    else:
        raise ValueError('alternative must be one of '
                         '["two-sided", "less", "greater"]')
    return(r, p)


def PToStars(p, Max=3):
    No = 0
    while p < 0.05 and No < Max:
        p *=10
        No +=1

    return(No)


def RAdjustNaNs(Array):
    try: NaN = RObj.NA_Real
    except NameError as e:
        raise e(f'[Analysis.Stats] {e}: Module `rpy2` not available.')

    for I, A in enumerate(Array):
        if A != A: Array[I] = NaN

    return(Array)


def RCheckPackage(Packages):
    try:
        RPacksToInstall = [Pack for Pack in Packages if not RPkg.isinstalled(Pack)]
    except NameError as e:
        raise e(f'[Analysis.Stats] {e}: Module `rpy2` not available.')

    if len(RPacksToInstall) > 0:
        print(f'[{ScriptName}] {str(RPacksToInstall)} not installed. Install now?')
        Ans = input('[y/N]: ')

        if Ans.lower() in ['y', 'yes']:
            from rpy2.robjects.vectors import StrVector as RStrVector

            RUtils = RPkg.importr('utils')
            RUtils.chooseCRANmirror(ind=1)

            RUtils.install_packages(RStrVector(RPacksToInstall))

        else: print(f'[{ScriptName}] Aborted.')

    return(None)


def RModelToDict(Model):
    Dict = {}
    Dict['l'] = []

    for C,Col in Model.items():
        try:
            Dict[C] = np.array(list(Col.iter_labels()))
        except AttributeError:
            if C is None and 'rpy2.robjects.vectors.DataFrame' in str(type(Col)):
                Dict['l'] += [{c: RModelToDict(col) for c,col in Col.items()}]
            elif 'rpy2.robjects.vectors.DataFrame' in str(type(Col)):
                Dict[C] = RModelToDict(Col)
            elif C is None:
                Dict = np.array(Col)
            else:
                Dict[C] = np.array(Col)
        except IndexError:
            continue

    if type(Dict) == dict:
        if not len(Dict['l']): del(Dict['l'])
        if list(Dict.keys()) == ['l']: Dict = Dict['l']

    return(Dict)


def sak(d):
    k = [_ for _ in SubAnovas if _ in d.keys()]
    k = k[0] if len(k) else None
    return(k)


def spk(d):
    k = [_ for _ in SubPWCs if _ in d.keys()]
    k = k[0] if len(k) else None
    return(k)


## Level 1
def _RFriedman(Data, Factor, Id, FactorName='Factor', FactorsGroupBy=[], FactorGBNames=[], pAdj='holm'):
    try:
        RCheckPackage(['rstatix']); RPkg.importr('rstatix')
    except NameError as e:
        raise e(f'[Analysis.Stats] {e}: Module `rpy2` not available.')

    if not len(FactorGBNames):
        FactorGBNames = [f'FactorGB{_+1}' for _ in range(len(FactorsGroupBy))]

    Values = RObj.FloatVector(Data)
    Idv = RObj.IntVector(Id)
    FactorsV = [RObj.FactorVector(_) for _ in [Factor]+FactorsGroupBy]
    Frame = {([FactorName]+FactorGBNames)[f]: F for f,F in enumerate(FactorsV)}
    Frame['Values'] = Values
    Frame['Id'] = Idv
    Frame = RObj.DataFrame(Frame)

    RObj.globalenv['Frame'] = Frame
    RObj.globalenv['Values'] = Values
    RObj.globalenv['Id'] = Idv
    for F,FFactor in enumerate(FactorsV):
        RObj.globalenv[([FactorName]+FactorGBNames)[F]] = FFactor

    fGB = f"group_by({','.join(FactorGBNames)}) %>%" if len(FactorsGroupBy) else ''

    Model = RObj.r(f'''Frame %>% {fGB} friedman_test(Values~{FactorName}|Id) %>% adjust_pvalue(method="{pAdj}")''')
    Modelc = RObj.r(f'''Frame %>% {fGB} friedman_effsize(Values~{FactorName}|Id)''')

    Result = {'Friedman': RModelToDict(Model), 'FriedmanEffect': RModelToDict(Modelc)}
    Result['Friedman']['Effect'] = np.array([FactorName]*len(Result['Friedman']['p']))
    return(Result)


def _RShapiro(Data, Factors, FactorNames=[], pAdj='holm'):
    FunctionName = inspect.stack()[0][3]
    try:
        RCheckPackage(['rstatix']); RPkg.importr('rstatix')
    except NameError as e:
        raise e(f'[Analysis.Stats] {e}: Module `rpy2` not available.')

    if not len(FactorNames):
        FactorNames = [f'Factor{_+1}' for _ in range(len(Factors))]

    Values = RObj.FloatVector(Data)
    FactorsV = [RObj.FactorVector(_) for _ in Factors]
    Frame = {FactorNames[f]: F for f,F in enumerate(FactorsV)}
    Frame['Values'] = Values
    Frame = RObj.DataFrame(Frame)

    RObj.globalenv['Frame'] = Frame
    RObj.globalenv['Values'] = Values
    for F,Factor in enumerate(FactorsV): RObj.globalenv[FactorNames[F]] = Factor

    try:
        Model = RObj.r(f'''Frame %>% group_by({','.join(FactorNames)}) %>% shapiro_test(Values) %>% adjust_pvalue(method="{pAdj}")''')
        Result = {f'{FunctionName}': RModelToDict(Model)}
    except Exception as e:
        print(f"[{ScriptName}.{FunctionName}] Cannot calculate test.")
        Result = {f'{FunctionName}': {}}


    return(Result)


def _RTTest(Data, Factor, Paired, FactorName='Factor', FactorsGroupBy=[], FactorGBNames=[], pAdj= "holm", EqualVar=False, Alt="two.sided", ConfLevel=0.95):
    try:
        RCheckPackage(['rstatix']); RPkg.importr('rstatix')
    except NameError as e:
        raise e(f'[Analysis.Stats] {e}: Module `rpy2` not available.')
        return(Result)

    if not len(FactorGBNames):
        FactorGBNames = [f'FactorGB{_+1}' for _ in range(len(FactorsGroupBy))]

    Values = RObj.FloatVector(Data)
    FactorsV = [RObj.FactorVector(_) for _ in [Factor]+FactorsGroupBy]
    Frame = {([FactorName]+FactorGBNames)[f]: F for f,F in enumerate(FactorsV)}
    Frame['Values'] = Values
    Frame = RObj.DataFrame(Frame)

    RObj.globalenv['Frame'] = Frame
    RObj.globalenv['Values'] = Values
    for F,FFactor in enumerate(FactorsV):
        RObj.globalenv[([FactorName]+FactorGBNames)[F]] = FFactor

    fGB = f"group_by({','.join(FactorGBNames)}) %>%" if len(FactorsGroupBy) else ''
    PairedV = 'TRUE' if Paired else 'FALSE'
    EqualVarV = 'TRUE' if EqualVar else 'FALSE'

    try:
        Modelt = RObj.r(f'''Frame %>% {fGB} pairwise_t_test(Values~{FactorName}, paired={PairedV}, var.equal={EqualVarV}, alternative="{Alt}", conf.level={ConfLevel}) %>% adjust_pvalue(method="{pAdj}")''')
    except:
        Modelt = RObj.r(f'''Frame %>% {fGB} pairwise_t_test(Values~{FactorName}, paired={PairedV}, alternative="{Alt}") %>% adjust_pvalue(method="{pAdj}")''')

    Modelc = RObj.r(f'''Frame %>% {fGB} cohens_d(Values~{FactorName}, conf.level={ConfLevel}, var.equal={EqualVarV}, paired={PairedV})''')

    Result = {'TTest': RModelToDict(Modelt), 'CohensD': RModelToDict(Modelc)}
    return(Result)


def _RWilcoxon(Data, Factor, Paired, FactorName='Factor', FactorsGroupBy=[], FactorGBNames=[], pAdj= "holm", Alt="two.sided", ConfLevel=0.95):
    try:
        RCheckPackage(['rstatix','coin']); RPkg.importr('rstatix')
    except NameError as e:
        raise e(f'[Analysis.Stats] {e}: Module `rpy2` not available.')

    if not len(FactorGBNames):
        FactorGBNames = [f'FactorGB{_+1}' for _ in range(len(FactorsGroupBy))]

    Values = RObj.FloatVector(Data)
    FactorsV = [RObj.FactorVector(_) for _ in [Factor]+FactorsGroupBy]
    Frame = {([FactorName]+FactorGBNames)[f]: F for f,F in enumerate(FactorsV)}
    Frame['Values'] = Values
    Frame = RObj.DataFrame(Frame)

    RObj.globalenv['Frame'] = Frame
    RObj.globalenv['Values'] = Values
    for F,FFactor in enumerate(FactorsV):
        RObj.globalenv[([FactorName]+FactorGBNames)[F]] = FFactor

    fGB = f"group_by({','.join(FactorGBNames)}) %>%" if len(FactorsGroupBy) else ''
    PairedV = 'TRUE' if Paired else 'FALSE'

    try:
        Modelt = RObj.r(f'''Frame %>% {fGB} pairwise_wilcox_test(Values~{FactorName}, paired={PairedV}, alternative="{Alt}", conf.level={ConfLevel}) %>% adjust_pvalue(method="{pAdj}")''')
    except:
        Modelt = RObj.r(f'''Frame %>% {fGB} pairwise_wilcox_test(Values~{FactorName}, paired={PairedV}, alternative="{Alt}") %>% adjust_pvalue(method="{pAdj}")''')

    Modelc = RObj.r(f'''Frame %>% {fGB} wilcox_effsize(Values~{FactorName}, conf.level={ConfLevel}, paired={PairedV}, alternative="{Alt}")''')

    Result = {'Wilcoxon': RModelToDict(Modelt), 'WilcoxonEffSize': RModelToDict(Modelc)}
    return(Result)


def Bartlett(Data, Factor, FactorName='Factor', FactorsGroupBy=[], FactorGBNames=[], pAdj='holm'):
    FunctionName = inspect.stack()[0][3]
    if not len(FactorGBNames):
        FactorGBNames = [f'FactorGB{_+1}' for _ in range(len(FactorsGroupBy))]

    Factor = np.array(Factor)
    Test = {}
    FLs = np.unique(Factor)
    if len(FLs) < 2:
        raise ValueError("The number of levels in `Factor` must be >1.")

    sf = sst.bartlett

    if len(FactorsGroupBy):
        Test = {**Test, **{_:[] for _ in FactorGBNames}}
        Test = {**Test, **{_:[] for _ in ('statistic','p')}}
        FacPr = tuple(product(*[np.unique(_) for _ in FactorsGroupBy]))

        for FC in FacPr:
            i = np.prod([FactorsGroupBy[l]==L for l,L in enumerate(FC)], axis=0, dtype=bool)
            iFLs = np.unique(Factor[i])
            if len(iFLs) < 2:
                raise ValueError("The number of levels in `Factor` must be >1.")

            In = [Data[i*(Factor==l)] for l in iFLs]
            s, p = sf(*In)
            pdes = PairwiseDescribe(Data[i], '')
            Test = MergeDictsAndContents(Test, pdes)
            Test['statistic'].append(s)
            Test['p'].append(p)

            for fn,FN in enumerate(FactorGBNames): Test[FN].append(FC[fn])

        Test = {k:np.array(v) for k,v in Test.items()}
        Test['p.adj'] = multipletests(Test['p'], method=pAdj)[1]

    else:
        In = [Data[Factor==l] for l in FLs]
        sp = np.array(sf(*In))
        Test = PairwiseDescribe(Data, '')
        Test['statistic'] = sp[:1]
        Test['p'] = sp[1:]
        Test['p.adj'] = sp[1:]

    Test['Effect'] = np.repeat([FactorName], len(Test['p']))
    Result = {FunctionName: {
        K:Test[K] for K in OrderKeys(Test, [FactorName]+list(FactorGBNames))
    }}
    return(Result)


def CohensD(Data, Factor):
    Test = PairwiseDescribe(Data, Factor)
    StDAll = (
        (
            (Test['n1'] - 1) * Test['var1'] +
            (Test['n2'] - 1) * Test['var2']
        ) / (Test['n1'] + Test['n2'] - 2)
    )**0.5
    Test['CohensD'] = (Test['mean1']-Test['mean2'])/StDAll
    return(Test)


def Friedman(Data, Factor, Id, FactorName='Factor', FactorsGroupBy=[], FactorGBNames=[], pAdj='holm'):
    FunctionName = inspect.stack()[0][3]

    if not len(FactorGBNames):
        FactorGBNames = [f'FactorGB{_+1}' for _ in range(len(FactorsGroupBy))]

    Factor = np.array(Factor)
    Test = {}
    FLs = np.unique(Factor)
    sf = sst.friedmanchisquare

    if len(FactorsGroupBy):
        Test = {**Test, **{_:[] for _ in FactorGBNames}}
        Test = {**Test, **{_:[] for _ in ('statistic','p')}}
        FacPr = tuple(product(*[np.unique(_) for _ in FactorsGroupBy]))

        for FC in FacPr:
            i = np.prod([FactorsGroupBy[l]==L for l,L in enumerate(FC)], axis=0, dtype=bool)
            iFLs = np.unique(Factor[i])
            s, p = sf(*[Data[i*(Factor==l)] for l in iFLs])

            pdes = PairwiseDescribe(Data[i], '')
            Test = MergeDictsAndContents(Test, pdes)
            Test['statistic'].append(s)
            Test['p'].append(p)

            for fn,FN in enumerate(FactorGBNames): Test[FN].append(FC[fn])

        Test = {k:np.array(v) for k,v in Test.items()}
        Test['p.adj'] = multipletests(Test['p'], method=pAdj)[1]

    else:
        sp = np.array(sf(*[Data[Factor==l] for l in FLs]))
        Test = PairwiseDescribe(Data, '')
        Test['statistic'] = sp[:1]
        Test['p'] = sp[1:]
        Test['p.adj'] = sp[1:]

    Test['KendallsWEffSize'] = KendallsW(
        Data, Factor, FactorName, FactorsGroupBy, FactorGBNames
    )
    Test['Effect'] = np.repeat([FactorName], len(Test['p']))

    Result = {FunctionName: {
        K:Test[K] for K in OrderKeys(Test, [FactorName]+list(FactorGBNames))
    }}

    return(Result)


def GetAnovaReport(Anova, FacNames):
    Report = []
    try:
        # if Anova[sak(Anova)]['p'].min()<0.05:
            # Report.append(f'''
        # {len(FacNames)}-way anova:
            # {Anova[sak(Anova)]['Effect'][Anova[sak(Anova)]['p']<0.05]},
            # F: {Anova[sak(Anova)]['F'][Anova[sak(Anova)]['p']<0.05]},
            # p: {['{:.1e}'.format(_) for _ in Anova[sak(Anova)]['p'][Anova[sak(Anova)]['p']<0.05]]}
        # ''')

        Report.append(f'{len(FacNames)}-way anova:\n')
        kvpk = 'p'
        fnl = tuple(FacNames)+('Effect',kvpk,'F')
        vfps = Anova[sak(Anova)][kvpk]
        kvpv = np.array([
            _ if _ is not None else np.nan
            for _ in Anova[sak(Anova)][kvpk]
        ])
        for k,v in Anova[sak(Anova)].items():
            if k in fnl and vfps.size and kvpv.min()<0.05:
                if k in ['p','p.adj']:
                    Report.append(f"{k}: {np.array(['{:.1e}'.format(_) for _ in v[kvpv<0.05]])}")
                else:
                    Report.append(f'{k}: {v[kvpv<0.05]}')

        if sak(Anova)+'Effect' in Anova.keys():
            if 'effsize' in Anova[sak(Anova)+'Effect']:
                Report.append(f"Eff. size: {Anova[sak(Anova)+'Effect']['effsize'][kvpv<0.05]}")

    except IndexError: pass
    except KeyError: pass

    if 'FXs' in Anova.keys():
        Report.append('\n'); Report.append('Sub anovas:\n')

        rd = {}
        for kf,vf in Anova['FXs'].items():
            if sak(vf) is None: continue

            kvpk = 'p.adj' if 'p.adj' in vf[sak(vf)] else 'p'
            fnl = tuple(FacNames)+('Effect',kvpk,'F')
            vfps = vf[sak(vf)][kvpk]
            kvpv = np.array([
                _ if _ is not None else np.nan
                for _ in vf[sak(vf)][kvpk]
            ])

            for k,v in vf[sak(vf)].items():
                if k in fnl and vfps.size and kvpv.min()<0.05:
                    if kf not in rd.keys(): rd[kf] = {}
                    if k in ['p','p.adj']:
                        rd[kf][k] = np.array(['{:.1e}'.format(_) for _ in v[kvpv<0.05]])
                    else:
                        rd[kf][k] = v[kvpv<0.05]

                    for esk in (sak(vf)+'EffSize', sak(vf)+'Effect'):
                        if esk in vf.keys():
                            rd[kf][esk] = vf[esk]['effsize'][kvpv<0.05].round(3)

        Report.append(Print(rd))


    if 'PWCs' in Anova.keys():
        Report.append('\n'); Report.append('Pairwise comparisons:\n')

        rd = {}
        for kf,vf in Anova['PWCs'].items():
            if spk(vf) is None: continue

            kvpk = 'p.adj' if 'p.adj' in vf[spk(vf)] else 'p'
            fnl = tuple(FacNames)+(
                'group1', 'group2', 'Effect', kvpk, 'F',
                'n1', 'n2', 'mean1', 'mean2', 'sem1', 'sem2'
            )
            vfps = vf[spk(vf)][kvpk]

            for k,v in vf[spk(vf)].items():
                if k in fnl and vfps.size and vfps.min()<0.05:
                    if kf not in rd.keys(): rd[kf] = {}
                    if k in ['p','p.adj']:
                        rd[kf][k] = np.array(['{:.1e}'.format(_) for _ in v[vfps<0.05]])
                    elif 'mean' in k or 'sem' in k:
                        rd[kf][k] = np.array([round(_,3) for _ in v[vfps<0.05]])
                    else:
                        rd[kf][k] = v[vfps<0.05]

                    for esk in (spk(vf)+'EffSize', spk(vf)+'Effect'):
                        if esk in vf.keys():
                            rd[kf][esk] = vf[esk]['effsize'][vfps<0.05].round(3)

        Report.append(Print(rd))

    Report.append('='*80); Report.append('\n')
    return(Report)


def HartigansDip(
        Data, FactorsGroupBy=[], FactorGBNames=[], isHist=False, TestNo=100,
        Alpha=0.05, GetAllIndices=False, pAdj='holm', Verbose=False
    ):
    FunctionName = inspect.stack()[0][3]

    if not Availunidip:
        raise ModuleNotFoundError(
            f"[{ScriptName}.{FunctionName}] Module `unidip` not available."
        )

    Test = PairwiseDescribe(Data, '', FactorsGroupBy, FactorGBNames)
    if Verbose:
        print(f"[{ScriptName}.{FunctionName}] Running {FunctionName} for {TestNo} iterations...")

    if len(FactorsGroupBy):
        Test = {**Test, **{_:[] for _ in FactorGBNames}}
        Test = {**Test, **{_:[] for _ in ('indices','dip','p')}}
        FacPr = tuple(product(*[np.unique(_) for _ in FactorsGroupBy]))

        for fc,FC in enumerate(FacPr):
            if Verbose: print(f"[{ScriptName}.{FunctionName}]     {fc+1} of {len(FacPr)}...")
            i = np.prod([FactorsGroupBy[l]==L for l,L in enumerate(FC)], axis=0, dtype=bool)
            Res = HartigansDip(Data[i], [], [], isHist, TestNo)

            for K in ('indices','dip','p'):
                Test[K].append(Res[FunctionName][K][0])

            for fn,FN in enumerate(FactorGBNames): Test[FN].append(FC[fn])

        Test = {k:np.array(v) for k,v in Test.items()}
        Test['p.adj'] = multipletests(Test['p'], method=pAdj)[1]

    else:
        Sorted = Data.copy() if isHist else np.msort(Data)
        Dip, p, Index = diptst(Sorted, is_hist=isHist, numt=TestNo)
        Test['dip'] = [Dip]
        Test['p'] = [p]
        if p < Alpha and GetAllIndices:
            if Verbose:
                print(f"[{ScriptName}.{FunctionName}]     Getting dip indices...")

            Index = UniDip(Sorted, is_hist=isHist, ntrials=TestNo, alpha=Alpha).run()

        # if p > Alpha: Index = []
        Index = np.array(Index)
        if len(Index.shape) == 1: Index = Index.reshape((Index.shape[0],1))
        Index = Index.T

        Test['indices'] = Index

    Res = {FunctionName: {K:Test[K] for K in OrderKeys(Test, FactorGBNames)}}
    Res[FunctionName] = {k:np.array(v) for k,v in Res[FunctionName].items()}

    if Verbose:
        print(f"[{ScriptName}.{FunctionName}] Done.")

    return(Res)


def KendallsW(Data, Factor, FactorName='Factor', FactorsGroupBy=[], FactorGBNames=[]):
    FunctionName = inspect.stack()[0][3]
    if not len(FactorGBNames):
        FactorGBNames = [f'FactorGB{_+1}' for _ in range(len(FactorsGroupBy))]

    Test = {}
    FLs = np.unique(Factor)
    if len(FLs) < 3:
        raise ValueError("The number of levels in `Factor` must be >2.")

    sf = _KendallsW

    if len(FactorsGroupBy):
        Test = {**Test, **{_:[] for _ in FactorGBNames}}
        Test = {**Test, **{_:[] for _ in ('W',)}}
        FacPr = tuple(product(*[np.unique(_) for _ in FactorsGroupBy]))

        for FC in FacPr:
            i = np.prod([FactorsGroupBy[l]==L for l,L in enumerate(FC)], axis=0, dtype=bool)
            iFLs = np.unique(Factor[i])
            if len(iFLs) < 3:
                raise ValueError("The number of levels in `Factor` must be >2.")

            W = sf(Data[i], Factor[i])
            pdes = PairwiseDescribe(Data[i], '')

            Test = MergeDictsAndContents(Test, pdes)
            Test['W'].append(W)

            for fn,FN in enumerate(FactorGBNames): Test[FN].append(FC[fn])

        Test = {k:np.array(v) for k,v in Test.items()}
        Test['p.adj'] = multipletests(Test['p'], method=pAdj)[1]

    else:
        W = sf(Data, Factor)
        Test = PairwiseDescribe(Data, '')
        Test['W'] = np.array([W])

    Test['Effect'] = np.repeat([FactorName], len(Test['W']))
    Result = {FunctionName: {
        K:Test[K] for K in OrderKeys(Test, [FactorName]+list(FactorGBNames))
    }}
    return(Result)


def KolmogorovSmirnov(Data, Factor='norm', FactorName='Factor', pAdj='holm', Alt="two.sided", Mode='auto'):
    FunctionName = inspect.stack()[0][3]

    Test = PairwiseDescribe(Data, Factor, [], [])
    sfa = {'alternative': Alt.replace('.','-'), 'mode': Mode}

    if type(Factor) == str:
        sp = np.array(sst.kstest(Data, Factor, **sfa))
    else:
        print(Factor, type(Factor))
        FLs = np.unique(Factor)
        if len(FLs) != 2:
            raise ValueError('The number of levels in `Factor` must be 2.')

        # sp = np.array(sst.ks_2samp(Data[Factor==FLs[0]], Data[Factor==FLs[1]], **sfa))
        sp = np.array(sst.kstest(Data[Factor==FLs[0]], Data[Factor==FLs[1]], **sfa))

    Test['statistic'] = sp[:1]
    Test['p'] = sp[1:]

    Result = {FunctionName: {K:Test[K] for K in OrderKeys(Test, [FactorName])}}

    return(Result)


def Levene(Data, Factor, FactorName='Factor', FactorsGroupBy=[], FactorGBNames=[], pAdj='holm'):
    FunctionName = inspect.stack()[0][3]
    if not len(FactorGBNames):
        FactorGBNames = [f'FactorGB{_+1}' for _ in range(len(FactorsGroupBy))]

    Factor = np.array(Factor)
    Test = {}
    FLs = np.unique(Factor)
    if len(FLs) < 2:
        raise ValueError("The number of levels in `Factor` must be >1.")

    sf = sst.levene

    if len(FactorsGroupBy):
        Test = {**Test, **{_:[] for _ in FactorGBNames}}
        Test = {**Test, **{_:[] for _ in ('df1','df2','statistic','p')}}
        FacPr = tuple(product(*[np.unique(_) for _ in FactorsGroupBy]))

        for FC in FacPr:
            i = np.prod([FactorsGroupBy[l]==L for l,L in enumerate(FC)], axis=0, dtype=bool)
            iFLs = np.unique(Factor[i])
            if len(iFLs) < 2:
                raise ValueError("The number of levels in `Factor` must be >1.")

            In = [Data[i*(Factor==l)] for l in iFLs]
            s, p = sf(*In)
            pdes = PairwiseDescribe(Data[i], '')
            Test = MergeDictsAndContents(Test, pdes)
            Test['df1'].append(len(In)-1)
            Test['df2'].append(sum([len(_) for _ in In]) - len(In))
            Test['statistic'].append(s)
            Test['p'].append(p)

            for fn,FN in enumerate(FactorGBNames): Test[FN].append(FC[fn])

        Test = {k:np.array(v) for k,v in Test.items()}
        Test['p.adj'] = multipletests(Test['p'], method=pAdj)[1]

    else:
        In = [Data[Factor==l] for l in FLs]
        sp = np.array(sf(*In))
        Test = PairwiseDescribe(Data, '')
        Test['df1'] = len(In)-1
        Test['df2'] = sum([len(_) for _ in In]) - len(In)
        Test['statistic'] = sp[:1]
        Test['p'] = sp[1:]
        Test['p.adj'] = sp[1:]

    Test['Effect'] = np.repeat([FactorName], len(Test['p']))
    Result = {FunctionName: {
        K:Test[K] for K in OrderKeys(Test, [FactorName]+list(FactorGBNames))
    }}
    return(Result)


def _RLevene(Data, Factor, FactorName='Factor', FactorsGroupBy=[], FactorGBNames=[], pAdj='holm'):
    FunctionName = inspect.stack()[0][3]
    try:
        RCheckPackage(['rstatix']); RPkg.importr('rstatix')
    except NameError as e:
        raise e(f'[Analysis.Stats] {e}: Module `rpy2` not available.')

    if not len(FactorGBNames):
        FactorGBNames = [f'FactorGB{_+1}' for _ in range(len(FactorsGroupBy))]

    Values = RObj.FloatVector(Data)
    FactorsV = [RObj.FactorVector(_) for _ in [Factor]+FactorsGroupBy]
    Frame = {([FactorName]+FactorGBNames)[f]: F for f,F in enumerate(FactorsV)}
    Frame['Values'] = Values
    Frame = RObj.DataFrame(Frame)

    RObj.globalenv['Frame'] = Frame
    RObj.globalenv['Values'] = Values
    for F,FFactor in enumerate(FactorsV):
        RObj.globalenv[([FactorName]+FactorGBNames)[F]] = FFactor

    fGB = f"group_by({','.join(FactorGBNames)}) %>%" if len(FactorsGroupBy) else ''

    try:
        Model = RObj.r(f'''Frame %>% {fGB} levene_test(Values~{FactorName}) %>% adjust_pvalue(method="{pAdj}")''')
        Result = {f'{FunctionName}': RModelToDict(Model)}
    except Exception as e:
        print(f"[{ScriptName}.{FunctionName}] Cannot calculate test.")
        Result = {f'{FunctionName}': {}}

    return(Result)


def KruskalWallis(Data, Factor, FactorName='Factor', FactorsGroupBy=[], FactorGBNames=[], pAdj='holm'):
    try:
        RCheckPackage(['rstatix']); RPkg.importr('rstatix')
    except NameError as e:
        raise e(f'[Analysis.Stats] {e}: Module `rpy2` not available.')

    if not len(FactorGBNames):
        FactorGBNames = [f'FactorGB{_+1}' for _ in range(len(FactorsGroupBy))]

    Values = RObj.FloatVector(Data)
    FactorsV = [RObj.FactorVector(_) for _ in [Factor]+FactorsGroupBy]
    Frame = {([FactorName]+FactorGBNames)[f]: F for f,F in enumerate(FactorsV)}
    Frame['Values'] = Values
    Frame = RObj.DataFrame(Frame)

    RObj.globalenv['Frame'] = Frame
    RObj.globalenv['Values'] = Values
    for F,FFactor in enumerate(FactorsV):
        RObj.globalenv[([FactorName]+FactorGBNames)[F]] = FFactor

    fGB = f"group_by({','.join(FactorGBNames)}) %>%" if len(FactorsGroupBy) else ''

    Model = RObj.r(f'''Frame %>% {fGB} kruskal_test(Values~{FactorName}) %>% adjust_pvalue(method="{pAdj}")''')
    Modelc = RObj.r(f'''Frame %>% {fGB} kruskal_effsize(Values~{FactorName})''')

    Result = {'KruskalWallis': RModelToDict(Model), 'KruskalWallisEffect': RModelToDict(Modelc)}
    Result['KruskalWallis']['Effect'] = np.array([FactorName]*len(Result['KruskalWallis']['p']))
    return(Result)


def PearsonCorr(
        Data, Factor, FactorName='Factor', FactorsGroupBy=[], FactorGBNames=[], pAdj= "holm"
    ):

    FunctionName = inspect.stack()[0][3]

    Factor = np.array(Factor)
    if not len(FactorGBNames):
        FactorGBNames = [f'FactorGB{_+1}' for _ in range(len(FactorsGroupBy))]

    FLs = np.unique(Factor)
    if len(FLs) < 2:
        raise ValueError(f'[{ScriptName}.{FunctionName}] The number of levels in `Factor` must be at least 2.')

    elif len(FLs) > 2:
        FLPairs = list(combinations(FLs,2))
        Res = []
        for FLPair in FLPairs:
            FLI = (Factor==FLPair[0])+(Factor==FLPair[1])
            Res.append(PearsonCorr(
                Data[FLI], Factor[FLI], FactorName,
                [_[FLI] for _ in FactorsGroupBy],
                FactorGBNames, pAdj
            ))

        Test = {}
        for c in Res:
            Test = MergeDictsAndContents(Test,c)

        Test = Test[FunctionName]
        Test['p.adj'] = multipletests(Test['p'], method=pAdj)[1]

    else:
        Test = PairwiseDescribe(Data, Factor, FactorsGroupBy, FactorGBNames)
        sf = sst.pearsonr
        sfa = {}

        if len(FactorsGroupBy):
            FacPr = tuple(product(*[np.unique(_) for _ in FactorsGroupBy]))
            for K in ('r','p'): Test[K] = []

            for FC in FacPr:
                i = np.prod([FactorsGroupBy[l]==L for l,L in enumerate(FC)], axis=0, dtype=bool)
                r, p = sf(Data[i*(Factor==FLs[0])], Data[i*(Factor==FLs[1])], **sfa)

                Test['r'].append(r)
                Test['p'].append(p)

            Test = {k:np.array(v) for k,v in Test.items()}
            Test['p.adj'] = multipletests(Test['p'], method=pAdj)[1]

        else:
            sp = np.array(sf(Data[Factor==FLs[0]], Data[Factor==FLs[1]], **sfa))
            Test['r'] = sp[:1]
            Test['p'] = sp[1:]
            Test['p.adj'] = sp[1:]

    Result = {FunctionName: {
        K:Test[K] for K in OrderKeys(Test, [FactorName]+list(FactorGBNames))
    }}

    return(Result)


def RPCA(Matrix):
    try:
        RCheckPackage(['stats']); Rstats = RPkg.importr('stats')
    except NameError as e:
        raise e(f'[Analysis.Stats] {e}: Module `rpy2` not available.')

    RMatrix = RObj.Matrix(Matrix)
    PCA = Rstats.princomp(RMatrix)
    return(PCA)


def RAnOVa(Data, Factors, Id, Paired, FactorNames=[], FactorsGroupBy=[], FactorGBNames=[], pAdj='holm'):
    try:
        RCheckPackage(['rstatix']); RPkg.importr('rstatix')
    except NameError as e:
        raise e(f'[Analysis.Stats] {e}: Module `rpy2` not available.')

    if not len(FactorNames):
        FactorNames = [f'Factor{_+1}' for _ in range(len(Factors))]
    if not len(FactorGBNames):
        FactorGBNames = [f'FactorGB{_+1}' for _ in range(len(FactorsGroupBy))]

    Values = RObj.FloatVector(Data)
    FactorsV = [RObj.FactorVector(_) for _ in Factors+FactorsGroupBy]
    Idv = RObj.IntVector(Id)

    Frame = {(list(FactorNames)+list(FactorGBNames))[f]: F for f,F in enumerate(FactorsV)}
    Frame['Id'] = Idv
    Frame['Values'] = Values
    Frame = RObj.DataFrame(Frame)

    RObj.globalenv['Frame'] = Frame
    RObj.globalenv['Id'] = Idv
    RObj.globalenv['Values'] = Values
    for F,FFactor in enumerate(FactorsV):
        RObj.globalenv[(list(FactorNames)+list(FactorGBNames))[F]] = FFactor

    FactorsW = ','.join([FactorNames[_] for _ in range(len(Factors)) if Paired[_]])
    FactorsB = ','.join([FactorNames[_] for _ in range(len(Factors)) if not Paired[_]])
    fGB = f"group_by({','.join(FactorGBNames)}) %>%" if len(FactorsGroupBy) else ''

    Model = RObj.r(f'''invisible(Frame %>% {fGB} anova_test(dv=Values, wid=Id, between=c({FactorsB}), within=c({FactorsW})) %>% adjust_pvalue(method="{pAdj}"))''')
    Result = RModelToDict(Model)

    if 'ANOVA' not in Result.keys() and 'anova' not in Result.keys(): Result = {'ANOVA': Result}
    if 'anova' in Result.keys() and 'ANOVA' not in Result.keys(): Result['ANOVA'] = Result.pop('anova')

    if type(Result['ANOVA']) == list:
        N = np.unique([len(_) for _ in Result.values()])
        if len(N) > 1:
            raise IndexError('All values should have the same length.')

        fKeys = {_ for _ in Result.keys() if _ != 'ANOVA'}
        a = {}
        for n in range(N[0]):
            rKeys = list(Result['ANOVA'][n].keys())
            if 'ANOVA' in rKeys:
                for k in rKeys:
                    if k not in a.keys(): a[k] = {}

                    sKeys = list(Result['ANOVA'][n][k].keys())
                    for s in sKeys:
                        if s not in a[k].keys(): a[k][s] = []
                        a[k][s].append(Result['ANOVA'][n][k][s])

                    for f in fKeys:
                        if f not in a[k].keys(): a[k][f] = []
                        a[k][f].append([Result[f][n]]*Result['ANOVA'][n][k][s].shape[0])
            else:
                if 'ANOVA' not in a.keys(): a['ANOVA'] = {}

                for k in rKeys:
                    if k not in a['ANOVA'].keys(): a['ANOVA'][k] = []
                    kn = Result['ANOVA'][n][k].shape[0] if len(Result['ANOVA'][n][k].shape) else 1

                    if kn==1:
                        a['ANOVA'][k].append([Result['ANOVA'][n][k]])
                    else:
                        a['ANOVA'][k].append(Result['ANOVA'][n][k])

                for f in fKeys:
                    if f not in a['ANOVA'].keys(): a['ANOVA'][f] = []
                    a['ANOVA'][f].append([Result[f][n]]*kn)


        Result = {K: {k: np.concatenate(v) for k,v in V.items()} for K,V in a.items()}

    return(Result)


def RAnOVaAfex(Data, Factors, Paired, Id=[], FactorNames=[]):
    try:
        RCheckPackage(['afex']); RPkg.importr('afex')
    except NameError as e:
        raise e(f'[Analysis.Stats] {e}: Module `rpy2` not available.')

    if not len(FactorNames):
        FactorNames = [f'Factor{_+1}' for _ in range(len(Factors))]

    Values = RObj.FloatVector(Data)
    FactorsV = [RObj.FactorVector(_) for _ in Factors]
    Frame = {FactorNames[f]: F for f,F in enumerate(FactorsV)}
    Frame['Values'] = Values

    if len(Id):
        Idv = RObj.IntVector(Id)
        RObj.globalenv['Id'] = Idv
        Frame['Id'] = Idv

    Frame = RObj.DataFrame(Frame)

    RObj.globalenv['Frame'] = Frame
    RObj.globalenv['Values'] = Values
    for F,Factor in enumerate(FactorsV): RObj.globalenv[FactorNames[F]] = Factor

    FactorsW = '*'.join([FactorNames[_] for _ in range(len(Factors)) if Paired[_]])
    FactorsAll = '*'.join(FactorNames)

    Model = RObj.r(f'''aov_car(Values ~ {FactorsAll} + Error(1|Id/({FactorsW})), Frame, na.rm=TRUE)''')
    Result = RModelToDict(Model)
    return(Result)


def RAnOVaPwr(GroupNo=None, SampleSize=None, Power=None,
           SigLevel=None, EffectSize=None):
    FunctionName = inspect.stack()[0][3]
    try:
        RCheckPackage(['pwr']); Rpwr = RPkg.importr('pwr')
    except NameError as e:
        raise e(f'[Analysis.Stats] {e}: Module `rpy2` not available.')

    if GroupNo is None: GroupNo = RObj.NULL
    if SampleSize is None: SampleSize = RObj.NULL
    if Power is None: Power = RObj.NULL
    if SigLevel is None: SigLevel = RObj.NULL
    if EffectSize is None: EffectSize = RObj.NULL

    Results = Rpwr.pwr_anova_test(k=GroupNo, power=Power, sig_level=SigLevel,
                                  f=EffectSize, n=SampleSize)

    print(f"[{ScriptName}.{FunctionName}] Running {Results.rx('method')[0][0]}...")
    AnOVaResults = {}
    for Key, Value in {'k': 'GroupNo', 'n': 'SampleSize', 'f': 'EffectSize',
                       'power':'Power', 'sig.level': 'SigLevel'}.items():
        AnOVaResults[Value] = Results.rx(Key)[0][0]

    print(f"[{ScriptName}.{FunctionName}] Done.")
    return(AnOVaResults)


def Shapiro(Data, Factors, FactorNames=[], pAdj='holm'):
    FunctionName = inspect.stack()[0][3]
    if not len(FactorNames):
        FactorNames = [f'Factor{_+1}' for _ in range(len(Factors))]

    Factors = [np.array(_) for _ in Factors]
    Test = {}
    sf = sst.shapiro

    Test = {**Test, **{_:[] for _ in FactorNames}}
    Test = {**Test, **{_:[] for _ in ('statistic','p')}}
    FacPr = tuple(product(*[np.unique(_) for _ in Factors]))

    for FC in FacPr:
        i = np.prod([Factors[l]==L for l,L in enumerate(FC)], axis=0, dtype=bool)
        s, p = sf(Data[i])

        pdes = PairwiseDescribe(Data[i], '')
        Test = MergeDictsAndContents(Test, pdes)
        Test['statistic'].append(s)
        Test['p'].append(p)

        for fn,FN in enumerate(FactorNames): Test[FN].append(FC[fn])

    Test = {k:np.array(v) for k,v in Test.items()}
    Test['p.adj'] = multipletests(Test['p'], method=pAdj)[1]

    Result = {FunctionName: {
        K:Test[K] for K in OrderKeys(Test, FactorNames)
    }}

    return(Result)



def TTest(
        Data, Factor, Paired, FactorName='Factor',
        FactorsGroupBy=[], FactorGBNames=[], pAdj= "holm", EqualVar=False,
        Alt="two.sided", ConfLevel=0.95
    ):
    FunctionName = inspect.stack()[0][3]

    Factor = np.array(Factor)
    if not len(FactorGBNames):
        FactorGBNames = [f'FactorGB{_+1}' for _ in range(len(FactorsGroupBy))]

    FLs = np.unique(Factor)
    if len(FLs) < 2:
        raise ValueError(f'[{ScriptName}.{FunctionName}] The number of levels in `Factor` must be at least 2.')

    elif len(FLs) > 2:
        FLPairs = list(combinations(FLs,2))
        Res = []
        for FLPair in FLPairs:
            FLI = (Factor==FLPair[0])+(Factor==FLPair[1])
            Res.append(TTest(
                Data[FLI], Factor[FLI], Paired, FactorName,
                [_[FLI] for _ in FactorsGroupBy],
                FactorGBNames, pAdj, EqualVar, Alt, ConfLevel
            ))

        Test = {}
        for c in Res:
            Test = MergeDictsAndContents(Test,c)

        Test = Test[FunctionName]
        Test['p.adj'] = multipletests(Test['p'], method=pAdj)[1]

    else:
        sf = sst.ttest_rel if Paired else sst.ttest_ind
        sfa = {'alternative': Alt.replace('.','-'), 'nan_policy':'omit'}
        if not Paired: sfa['equal_var'] = EqualVar

        Test = PairwiseDescribe(Data, Factor, FactorsGroupBy, FactorGBNames)

        if len(FactorsGroupBy):
            FacPr = tuple(product(*[np.unique(_) for _ in FactorsGroupBy]))
            for K in ('statistic','p','CohensDEffSize'): Test[K] = []

            for FC in FacPr:
                i = np.prod([FactorsGroupBy[l]==L for l,L in enumerate(FC)], axis=0, dtype=bool)
                s, p = sf(Data[i*(Factor==FLs[0])], Data[i*(Factor==FLs[1])], **sfa)

                Test['statistic'].append(s)
                Test['p'].append(p)
                Test['CohensDEffSize'].append(CohensD(Data[i], Factor[i])['CohensD'][0])

            Test = {k:np.array(v) for k,v in Test.items()}
            Test['p.adj'] = multipletests(Test['p'], method=pAdj)[1]

        else:
            sp = np.array(sf(Data[Factor==FLs[0]], Data[Factor==FLs[1]], **sfa))
            Test['statistic'] = sp[:1]
            Test['p'] = sp[1:]
            Test['p.adj'] = sp[1:]
            Test['CohensDEffSize'] = CohensD(Data, Factor)['CohensD']

        Test['df'] = Test['n1']-1

    Result = {FunctionName: {
        K:Test[K] for K in OrderKeys(Test, [FactorName]+list(FactorGBNames))
    }}

    return(Result)


def WelchAnOVa(Data, Factor, FactorName='Factor', FactorsGroupBy=[], FactorGBNames=[], pAdj='holm'):
    try:
        RCheckPackage(['rstatix']); RPkg.importr('rstatix')
    except NameError as e:
        raise e(f'[Analysis.Stats] {e}: Module `rpy2` not available.')

    if not len(FactorGBNames):
        FactorGBNames = [f'FactorGB{_+1}' for _ in range(len(FactorsGroupBy))]

    Values = RObj.FloatVector(Data)
    FactorsV = [RObj.FactorVector(_) for _ in [Factor]+FactorsGroupBy]
    Frame = {([FactorName]+FactorGBNames)[f]: F for f,F in enumerate(FactorsV)}
    Frame['Values'] = Values
    Frame = RObj.DataFrame(Frame)

    RObj.globalenv['Frame'] = Frame
    RObj.globalenv['Values'] = Values
    for F,FFactor in enumerate(FactorsV):
        RObj.globalenv[([FactorName]+FactorGBNames)[F]] = FFactor

    fGB = f"group_by({','.join(FactorGBNames)}) %>%" if len(FactorsGroupBy) else ''

    Model = RObj.r(f'''Frame %>% {fGB} welch_anova_test(Values~{FactorName}) %>% adjust_pvalue(method="{pAdj}")''')
    Result = {'WelchAnOVa': RModelToDict(Model)}
    if 'Effect' not in Result['WelchAnOVa'].keys():
        Result['WelchAnOVa']['Effect'] = np.array([FactorName for _ in Result['WelchAnOVa']['p']])

    return(Result)


def MannWhitneyU(
        Data, Factor, FactorName='Factor', FactorsGroupBy=[],
        FactorGBNames=[], pAdj= "holm", Alt="two.sided", ConfLevel=0.95
    ):

    sfk = inspect.stack()[0][3]

    Factor = np.array(Factor)
    if not len(FactorGBNames):
        FactorGBNames = [f'FactorGB{_+1}' for _ in range(len(FactorsGroupBy))]

    FLs = np.unique(Factor)
    if len(FLs) < 2:
        raise ValueError(f'[{ScriptName}.{sfk}] The number of levels in `Factor` must be at least 2.')

    elif len(FLs) > 2:
        FLPairs = list(combinations(FLs,2))
        Res = []
        for FLPair in FLPairs:
            FLI = (Factor==FLPair[0])+(Factor==FLPair[1])
            Res.append(MannWhitneyU(
                Data[FLI], Factor[FLI], FactorName,
                [_[FLI] for _ in FactorsGroupBy],
                FactorGBNames, pAdj, Alt, ConfLevel
            ))

        Test = {}
        for c in Res:
            Test = MergeDictsAndContents(Test,c)

        Test = Test[sfk]
        Test['p.adj'] = multipletests(Test['p'], method=pAdj)[1]

    else:
        sf = sst.mannwhitneyu
        sfa = {'alternative': Alt.replace('.','-'), 'nan_policy':'omit'}

        Test = PairwiseDescribe(Data, Factor, FactorsGroupBy, FactorGBNames)

        if len(FactorsGroupBy):
            FacPr = tuple(product(*[np.unique(_) for _ in FactorsGroupBy]))
            for K in ('t-statistic','z-statistic','p'): Test[K] = []

            for FC in FacPr:
                i = np.prod([FactorsGroupBy[l]==L for l,L in enumerate(FC)], axis=0, dtype=bool)
                s, p = sf(Data[i*(Factor==FLs[0])], Data[i*(Factor==FLs[1])], **sfa)
                z = sst.norm.isf(p/2)

                Test['t-statistic'].append(s)
                Test['z-statistic'].append(z)
                Test['p'].append(p)

            Test = {k:np.array(v) for k,v in Test.items()}
            Test['p.adj'] = multipletests(Test['p'], method=pAdj)[1]

        else:
            sp = np.array(sf(Data[Factor==FLs[0]], Data[Factor==FLs[1]], **sfa))
            z = sst.norm.isf(sp[1]/2)
            Test['t-statistic'] = sp[:1]
            Test['z-statistic'] = np.array([z])
            Test['p'] = sp[1:]
            Test['p.adj'] = sp[1:]

    Result = {sfk: {
        K:Test[K] for K in OrderKeys(Test, [FactorName]+list(FactorGBNames))
    }}
    EffSizeN = Result[sfk]['n1']+Result[sfk]['n2']
    Result[sfk]['effsize'] = Result[sfk]['z-statistic']/(EffSizeN**0.5)

    return(Result)


def Wilcoxon(
        Data, Factor, FactorName='Factor', FactorsGroupBy=[],
        FactorGBNames=[], pAdj= "holm", Alt="two.sided", ConfLevel=0.95
    ):

    sfk = inspect.stack()[0][3]

    Factor = np.array(Factor)
    if not len(FactorGBNames):
        FactorGBNames = [f'FactorGB{_+1}' for _ in range(len(FactorsGroupBy))]

    FLs = np.unique(Factor)
    if len(FLs) < 2:
        raise ValueError(f'[{ScriptName}.{sfk}] The number of levels in `Factor` must be at least 2.')

    elif len(FLs) > 2:
        FLPairs = list(combinations(FLs,2))
        Res = []
        for FLPair in FLPairs:
            FLI = (Factor==FLPair[0])+(Factor==FLPair[1])
            Res.append(Wilcoxon(
                Data[FLI], Factor[FLI], FactorName,
                [_[FLI] for _ in FactorsGroupBy],
                FactorGBNames, pAdj, Alt, ConfLevel
            ))

        Test = {}
        for c in Res:
            Test = MergeDictsAndContents(Test,c)

        Test = Test[sfk]
        Test['p.adj'] = multipletests(Test['p'], method=pAdj)[1]

    else:
        sf = sst.wilcoxon
        sfa = {'alternative': Alt.replace('.','-'), 'nan_policy':'omit'}

        Test = PairwiseDescribe(Data, Factor, FactorsGroupBy, FactorGBNames)

        if len(FactorsGroupBy):
            FacPr = tuple(product(*[np.unique(_) for _ in FactorsGroupBy]))
            for K in ('t-statistic','z-statistic','p'): Test[K] = []

            for FC in FacPr:
                i = np.prod([FactorsGroupBy[l]==L for l,L in enumerate(FC)], axis=0, dtype=bool)
                s, p = sf(Data[i*(Factor==FLs[0])], Data[i*(Factor==FLs[1])], **sfa)
                z = sst.norm.isf(p/2)

                Test['t-statistic'].append(s)
                Test['z-statistic'].append(z)
                Test['p'].append(p)

            Test = {k:np.array(v) for k,v in Test.items()}
            Test['p.adj'] = multipletests(Test['p'], method=pAdj)[1]

        else:
            sp = np.array(sf(Data[Factor==FLs[0]], Data[Factor==FLs[1]], **sfa))
            z = sst.norm.isf(sp[1]/2)
            Test['t-statistic'] = sp[:1]
            Test['z-statistic'] = np.array([z])
            Test['p'] = sp[1:]
            Test['p.adj'] = sp[1:]

    Result = {sfk: {
        K:Test[K] for K in OrderKeys(Test, [FactorName]+list(FactorGBNames))
    }}
    EffSizeN = Result[sfk]['n1']
    Result[sfk]['effsize'] = Result[sfk]['z-statistic']/(EffSizeN**0.5)

    return(Result)


## Level 2
def PairwiseComp(Data, Factor, Paired, Parametric='auto', FactorName='Factor', FactorsGroupBy=[], FactorGBNames=[], pAdj='holm', Alt="two.sided", ConfLevel=0.95):
    FunctionName = inspect.stack()[0][3]
    Results = {}

    if Parametric == 'auto':
        IsNormal = Shapiro(Data, [Factor], [FactorName], pAdj)
        if 'p.adj' in IsNormal['Shapiro'].keys():
            Results = {**Results,**IsNormal}
            IsNormal = IsNormal['Shapiro']['p.adj'].min()>0.05
        else:
            print(f"[{ScriptName}.{FunctionName}] Assuming normally-distributed samples.")
            IsNormal = True

    else:
        IsNormal = Parametric

    IsEqVar = Levene(Data, Factor, FactorName, pAdj=pAdj)
    if 'p.adj' in IsEqVar['Levene'].keys():
        Results.update(IsEqVar)
        IsEqVar = IsEqVar['Levene']['p.adj'].min()>0.05
    else:
        print(f"[{ScriptName}.{FunctionName}] Assuming unequal variances.")
        IsEqVar = False


    IM = IsMatched(Factor, Paired, FactorsGroupBy)

    if IsNormal:
        PWCs = TTest(
            Data, Factor, IM, FactorName, FactorsGroupBy, FactorGBNames, EqualVar=IsEqVar, pAdj=pAdj
        )
    else:
        if Paired and IM:
            PWCs = Wilcoxon(
                Data, Factor, FactorName, FactorsGroupBy, FactorGBNames, pAdj=pAdj
            )
        else:
            if Paired and not IM:
                print(f"[{ScriptName}.{FunctionName}] Data paired but not balanced. Assuming independent samples.")
            PWCs = MannWhitneyU(
                Data, Factor, FactorName, FactorsGroupBy, FactorGBNames, pAdj=pAdj
            )

    Results = {**Results, **PWCs}

    return(Results)


## Level 3
def AnOVa(Data, Factors, Id, Paired=[], Parametric='auto', FactorNames=[], GetAllPairwise=True, GetInvalidPWCs=True, pAdj='holm'):
    FunctionName = inspect.stack()[0][3]
    Results = {}

    Factors = [np.array(_) for _ in Factors]
    if not len(Paired):
        print(f"[{ScriptName}.{FunctionName}] Assuming all factors are between-subject (unpaired).")
        Paired = [False for _ in Factors]

    if not len(FactorNames):
        FactorNames = [f'Factor{_+1}' for _ in range(len(Factors))]

    if 'int' not in str(type(Id[0])):
        _, Id = np.unique(Id,return_inverse=True)

    Factors = list(Factors)
    for F,Factor in enumerate(Factors):
        if 'str' not in str(type(Factor[0])):
            Factors[F] = np.array(Factor).astype(str)

    # Get full anova
    print(f"[{ScriptName}.{FunctionName}] Getting full AnOVa...")
    if Parametric == 'auto':
        IsNormal = Shapiro(Data, Factors, FactorNames, pAdj)
        if 'p.adj' in IsNormal['Shapiro'].keys():
            Results = {**Results,**IsNormal}
            IsNormal = IsNormal['Shapiro']['p.adj'].min()>0.05
        else:
            print(f"[{ScriptName}.{FunctionName}] Assuming normally-distributed samples.")
            IsNormal = True

    else:
        IsNormal = Parametric

    try:
        if len(Factors) == 1:
            IsEqVarL = Levene(Data, Factors[0], FactorNames[0], pAdj=pAdj)
            if 'p.adj' in IsEqVarL['Levene'].keys():
                IsEqVar = IsEqVarL['Levene']['p.adj'].min()>0.05
            else:
                print(f"[{ScriptName}.{FunctionName}] Assuming unequal variances.")
                IsEqVar = False


            IM = IsMatched(Factors[0], Paired[0])

            if IsNormal and IsEqVar:
                aFull = RAnOVa(Data, Factors, Id, Paired, FactorNames, pAdj=pAdj)
            elif IsNormal and not IsEqVar:
                aFull = WelchAnOVa(Data, Factors[0], FactorNames[0], pAdj=pAdj)
            elif IM:
                try:
                    aFull = Friedman(Data, Factors[0], Id, FactorNames[0], pAdj=pAdj)
                except Exception as e:
                    aFull = KruskalWallis(Data, Factors[0], FactorNames[0], pAdj=pAdj)
            else:
                aFull = KruskalWallis(Data, Factors[0], FactorNames[0], pAdj=pAdj)

            if 'p.adj' in IsEqVarL['Levene'].keys(): aFull.update(IsEqVarL)

        else:
            aFull = RAnOVa(Data, Factors, Id, Paired, FactorNames, pAdj=pAdj)
    except Exception as e:
        print(f"[{ScriptName}.{FunctionName}] Cannot calculate statistics for all factors. Getting all pairwises.")
        aFull = {'ANOVA':{'Effect':[
            ':'.join(_)
            for a in range(len(FactorNames)-1)
            for _ in combinations(FactorNames,a+1)
        ]}}
        GetAllPairwise = True

    Results = {**Results,**aFull}
    aFk = sak(Results)

    # Get sub anovas based on significant effects
    FactorsWi = [_ for _ in range(len(FactorNames)) if Paired[_]]
    FactorsBi = [_ for _ in range(len(FactorNames)) if not Paired[_]]
    FactorsW = [FactorNames[_] for _ in FactorsWi]
    FactorsB = [FactorNames[_] for _ in FactorsBi]

    if GetAllPairwise:
        FullpsFacOrder = sorted(
            [_.split(':') for _ in Results[aFk]['Effect']],
            key=lambda x:len(x), reverse=True
        )
        FullpsFacOrder = [sorted(FullpsFacOrder[0])]+[
            sorted(p) if len(p)>1 else p for p in FullpsFacOrder[1:]
        ]
    else:
        if type(Results[aFk]) == dict:
            FullpsFacOrder = GetSigEff(Results[aFk])
        else:
            raise TypeError('This should be a dict. Check R output')

    FullpsFacOrder = [_ for _ in FullpsFacOrder if len(_) != len(Factors)]
    ToRun = FullpsFacOrder.copy()
    SubCs, PWCs = {}, {}

    if len(Factors) == 1:
        print(f"[{ScriptName}.{FunctionName}] Getting pairwise comparisons...")
        PWCs[FactorNames[0]] = PairwiseComp(Data, Factors[0], Paired[0], IsNormal, FactorNames[0], pAdj=pAdj)
    else:
        print(f"[{ScriptName}.{FunctionName}] Getting sub-AnOVas and pairwise comparisons...")
        while len(ToRun):
            PS = ToRun[0]
            PSs = ':'.join(PS)

            psGB = [Factors[FactorNames.index(_)] for _ in FactorNames if _ not in PS]
            psGBNames = [_ for _ in FactorNames if _ not in PS]
            psWB = [Factors[FactorNames.index(_)] for _ in PS]
            psPaired = [Paired[FactorNames.index(_)] for _ in PS]

            if len(PS) == 1:
                FInd = FactorNames.index(PS[0])

                IsEqVarL = Levene(Data, Factors[FInd], PSs, psGB, psGBNames, pAdj)
                if 'p.adj' in IsEqVarL['Levene'].keys():
                    IsEqVar = IsEqVarL['Levene']['p.adj'].min()>0.05
                else:
                    print(f"[{ScriptName}.{FunctionName}]     Assuming unequal variances.")
                    IsEqVar = False

                IM = IsMatched(Factors[FInd], Paired[FInd], psGB)
                msg = f"[{ScriptName}.{FunctionName}]     Not enough data to run FX for {PSs}"

                if IsEqVar and IsNormal:
                    try:
                        SubCs[PSs] = RAnOVa(Data, psWB, Id, psPaired, PS, psGB, psGBNames, pAdj=pAdj)
                    except Exception as e:
                        try:
                            if psPaired:
                                SubCs[PSs] = Friedman(Data, Factors[FInd], Id, PSs, psGB, psGBNames, pAdj=pAdj)
                            else:
                                SubCs[PSs] = WelchAnOVa(Data, Factors[FInd], PSs, psGB, psGBNames, pAdj=pAdj)
                        except Exception as e:
                            if not psPaired:
                                try:
                                    SubCs[PSs] = KruskalWallis(Data, Factors[FInd], PSs, psGB, psGBNames, pAdj=pAdj)
                                except Exception as e:
                                    print(msg)
                            else:
                                print(msg)

                elif IsNormal and not IsEqVar:
                    try:
                        if psPaired:
                            SubCs[PSs] = Friedman(Data, Factors[FInd], Id, PSs, psGB, psGBNames, pAdj=pAdj)
                        else:
                            SubCs[PSs] = WelchAnOVa(Data, Factors[FInd], PSs, psGB, psGBNames, pAdj=pAdj)
                    except Exception as e:
                        if not psPaired:
                            try:
                                SubCs[PSs] = KruskalWallis(Data, Factors[FInd], PSs, psGB, psGBNames, pAdj=pAdj)
                            except Exception as e:
                                print(msg)
                        else:
                            print(msg)
                else:
                    try:
                        if psPaired:
                            SubCs[PSs] = Friedman(Data, Factors[FInd], Id, PSs, psGB, psGBNames, pAdj=pAdj)
                        else:
                            SubCs[PSs] = KruskalWallis(Data, Factors[FInd], PSs, psGB, psGBNames, pAdj=pAdj)
                    except Exception as e:
                        print(msg)

                PWCs[PSs] = PairwiseComp(Data, Factors[FInd], Paired[FInd], IsNormal, PSs, psGB, psGBNames, pAdj)
                if PSs in SubCs.keys() and 'p.adj' in IsEqVarL['Levene'].keys():
                    SubCs[PSs].update(IsEqVarL)

            else:
                try:
                    SubCs[PSs] = RAnOVa(Data, psWB, Id, psPaired, PS, psGB, psGBNames, pAdj=pAdj)
                except Exception as e:
                    print(f"[{ScriptName}.{FunctionName}]     Not enough data to run FX for {PSs}.")

            if PSs in SubCs.keys():
                scKey = [_ for _ in SubAnovas if _ in SubCs[PSs].keys()][0]
                if type(SubCs[PSs][scKey]) == dict:
                    if 'Effect' in SubCs[PSs][scKey].keys():
                        pssFacOrder = GetSigEff(SubCs[PSs][scKey])
                    else:
                        pssFacOrder = []
                else:
                    raise TypeError('This should be a dict. Check R output')
            else:
                SubCs[PSs] = {}
                pssFacOrder = []

            if not len(pssFacOrder):
                pssFacOrder = [
                    sorted(_)
                    for _ in tuple(combinations(PS, len(PS)-1))
                ]
            else:
                pssFacOrder = [sorted(pssFacOrder[0])] + [
                    sorted(_)
                    for p in pssFacOrder
                    for _ in tuple(combinations(p, len(p)-1))
                ]

            ToRun = [
                _
                for _ in ToRun+pssFacOrder
                if ':'.join(_) not in SubCs.keys()
                and len(_)
            ]

    # Remove invalid comparisons
    if not GetAllPairwise or not GetInvalidPWCs:
        for PS in FullpsFacOrder:
            PSs = ':'.join(PS)

            FacLevelsValid = {
                _: np.unique(SubCs[PSs][sak(SubCs[PSs])][_][SubCs[PSs][sak(SubCs[PSs])]['p']<0.05])
                for _ in FactorNames if _ in SubCs[PSs][sak(SubCs[PSs])].keys()
            }

            SubFLV = {
                k: {
                    _: np.unique(SubCs[k][sak(SubCs[k])][_][SubCs[k][sak(SubCs[k])]['p']<0.05])
                    for _ in FactorNames if _ in SubCs[k][sak(SubCs[k])].keys()
                }
                for k in SubCs.keys()
                if k!= PSs
                and False not in (_ in PSs.split(':') for _ in k.split(':'))
            }

            SubKeys =  tuple(SubFLV.keys())

            SubFLV = {
                kk: vv
                for k,v in SubFLV.items() if ':' in k
                for kk,vv in v.items() if kk not in FacLevelsValid.keys()
            }

            FacLevelsValid = {**FacLevelsValid, **SubFLV}

            FLVInd = {
                k: [
                    np.array([_ in vv for _ in SubCs[k][sak(SubCs[k])][kk]])
                    for kk,vv in FacLevelsValid.items() if kk in SubCs[k][sak(SubCs[k])]
                ]
                for k in SubKeys
            }

            FLVIndPWC = {
                k: [
                    np.array([_ in vv for _ in PWCs[k][spk(PWCs[k])][kk]])
                    for kk,vv in FacLevelsValid.items() if kk in PWCs[k][spk(PWCs[k])]
                ]
                for k in SubKeys
                if k in PWCs.keys()
            }

            FLVInd = {k: np.prod(v, axis=0).astype(bool) for k,v in FLVInd.items()}
            FLVIndPWC = {k: np.prod(v, axis=0).astype(bool) for k,v in FLVIndPWC.items()}

            SubCs = {**SubCs, **{
                ksub: {
                        ktest: {
                            keff: veff[FLVInd[ksub]] if 'ndarray' in str(type(veff)) else veff for keff,veff in vtest.items()
                        }
                        if ktest in SubAnovas else vtest
                        for ktest,vtest in vsub.items()
                    }
                    if ksub in FLVInd.keys() else vsub
                for ksub,vsub in SubCs.items()
            }}

            PWCs = {**PWCs, **{
                ksub: {
                        ktest: {
                            keff: veff[FLVIndPWC[ksub]] for keff,veff in vtest.items()
                        }
                        for ktest,vtest in vsub.items()
                    }
                    if ksub in FLVInd.keys() else vsub
                for ksub,vsub in PWCs.items()
            }}

    if len(SubCs): Results['FXs'] = {**SubCs}
    if len(PWCs): Results['PWCs'] = {**PWCs}

    print(f"[{ScriptName}.{FunctionName}] Done.")
    return(Results)


