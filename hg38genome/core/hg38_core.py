from typing import Dict, List, Tuple
from ailist import LabeledIntervalArray
from intervalframe import IntervalFrame
import numpy as np
import os

# Local imports
from .seq_utils import *
from .interval_utils import *
from ..data.import_data import get_data_file


def get_include():
	"""
	Get file directory if C headers

	Parameters
	----------
		None

	Returns
	-------
		location : str
			Directory to header files
	"""

	# Grab file location
	location = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

	return location


class feature_finder(object):
    """
    """

    def __init__(self,
                 feature: str,
                 upstream: int = 0,
                 downstream: int = 0):
        """
        """
        
        feature_map = {"CTCF": get_ctcf,
                       "CpG_islands": get_cpg_islands}
        self.func = feature_map[feature]
        self.upstream = upstream
        self.downstream = downstream

    
    def __getitem__(self, key):
        """
        """

        feature_iframe = self.func(key, self.upstream, self.downstream)
        
        return feature_iframe


class gene_info_finder(object):
    """
    """

    def __init__(self,
                 feature: str,
                 upstream: int = 0,
                 downstream: int = 0,
                 gene_type: str = "all"):
        """
        """
        
        info_map = {"exons": get_exons,
                    "tss": get_tss,
                    "gene_body": get_gene_body}
        self.func = feature_map[feature]
        self.upstream = upstream
        self.downstream = downstream
        self.gene_type = gene_type

    
    def __getitem__(self, key):
        """
        """

        info_iframe = self.func(key, self.upstream, self.downstream, self.gene_type)
        
        return info_iframe

    
class cpg_finder(object):
    """
    """

    def __init__(self,
                 upstream: int = 0,
                 downstream: int = 0):
        """
        """
        
        self.func = get_cpgs
        self.upstream = upstream
        self.downstream = downstream

    
    def __getitem__(self, key):
        """
        """

        cpg_iframe = self.func(key, self.upstream, self.downstream)
        
        return cpg_iframe


class Hg38Genome(object):
    """
    Genome object for hg38
    """

    def __init__(self):
        """
        Initialize genome object
        """
        
        self.version = "hg38"
        self.n_CpGs = 28217448
        self.n_bases = 3137161264
        self.chrom_sizes = {"chr1":248956422,
                            "chr2":242193529,
                            "chr3":198295559,
                            "chr4":190214555,
                            "chr5":181538259,
                            "chr6":170805979,
                            "chr7":159345973,
                            "chr8":145138636,
                            "chr9":138394717,
                            "chr10":133797422,
                            "chr11":135086622,
                            "chr12":133275309,
                            "chr13":114364328,
                            "chr14":107043718,
                            "chr15":101991189,
                            "chr16":90338345,
                            "chr17":83257441,
                            "chr18":80373285,
                            "chr19":58617616,
                            "chr20":64444167,
                            "chr21":46709983,
                            "chr22":50818468,
                            "chrX":156040895,
                            "chrY":57227415,
                            "chrM":16569,
                            "chr1_KI270706v1_random":175055,
                            "chr1_KI270707v1_random":32032,
                            "chr1_KI270708v1_random":127682,
                            "chr1_KI270709v1_random":66860,
                            "chr1_KI270710v1_random":40176,
                            "chr1_KI270711v1_random":42210,
                            "chr1_KI270712v1_random":176043,
                            "chr1_KI270713v1_random":40745,
                            "chr1_KI270714v1_random":41717,
                            "chr2_KI270715v1_random":161471,
                            "chr2_KI270716v1_random":153799,
                            "chr3_GL000221v1_random":155397,
                            "chr4_GL000008v2_random":209709,
                            "chr5_GL000208v1_random":92689,
                            "chr9_KI270717v1_random":40062,
                            "chr9_KI270718v1_random":38054,
                            "chr9_KI270719v1_random":176845,
                            "chr9_KI270720v1_random":39050,
                            "chr11_KI270721v1_random":100316,
                            "chr14_GL000009v2_random":201709,
                            "chr14_GL000225v1_random":211173,
                            "chr14_KI270722v1_random":194050,
                            "chr14_GL000194v1_random":191469,
                            "chr14_KI270723v1_random":38115,
                            "chr14_KI270724v1_random":39555,
                            "chr14_KI270725v1_random":172810,
                            "chr14_KI270726v1_random":43739,
                            "chr15_KI270727v1_random":448248,
                            "chr16_KI270728v1_random":1872759,
                            "chr17_GL000205v2_random":185591,
                            "chr17_KI270729v1_random":280839,
                            "chr17_KI270730v1_random":112551,
                            "chr22_KI270731v1_random":150754,
                            "chr22_KI270732v1_random":41543,
                            "chr22_KI270733v1_random":179772,
                            "chr22_KI270734v1_random":165050,
                            "chr22_KI270735v1_random":42811,
                            "chr22_KI270736v1_random":181920,
                            "chr22_KI270737v1_random":103838,
                            "chr22_KI270738v1_random":99375,
                            "chr22_KI270739v1_random":73985,
                            "chrY_KI270740v1_random":37240,
                            "chrUn_KI270302v1":2274,
                            "chrUn_KI270304v1":2165,
                            "chrUn_KI270303v1":1942,
                            "chrUn_KI270305v1":1472,
                            "chrUn_KI270322v1":21476,
                            "chrUn_KI270320v1":4416,
                            "chrUn_KI270310v1":1201,
                            "chrUn_KI270316v1":1444,
                            "chrUn_KI270315v1":2276,
                            "chrUn_KI270312v1":998,
                            "chrUn_KI270311v1":12399,
                            "chrUn_KI270317v1":37690,
                            "chrUn_KI270412v1":1179,
                            "chrUn_KI270411v1":2646,
                            "chrUn_KI270414v1":2489,
                            "chrUn_KI270419v1":1029,
                            "chrUn_KI270418v1":2145,
                            "chrUn_KI270420v1":2321,
                            "chrUn_KI270424v1":2140,
                            "chrUn_KI270417v1":2043,
                            "chrUn_KI270422v1":1445,
                            "chrUn_KI270423v1":981,
                            "chrUn_KI270425v1":1884,
                            "chrUn_KI270429v1":1361,
                            "chrUn_KI270442v1":392061,
                            "chrUn_KI270466v1":1233,
                            "chrUn_KI270465v1":1774,
                            "chrUn_KI270467v1":3920,
                            "chrUn_KI270435v1":92983,
                            "chrUn_KI270438v1":112505,
                            "chrUn_KI270468v1":4055,
                            "chrUn_KI270510v1":2415,
                            "chrUn_KI270509v1":2318,
                            "chrUn_KI270518v1":2186,
                            "chrUn_KI270508v1":1951,
                            "chrUn_KI270516v1":1300,
                            "chrUn_KI270512v1":22689,
                            "chrUn_KI270519v1":138126,
                            "chrUn_KI270522v1":5674,
                            "chrUn_KI270511v1":8127,
                            "chrUn_KI270515v1":6361,
                            "chrUn_KI270507v1":5353,
                            "chrUn_KI270517v1":3253,
                            "chrUn_KI270529v1":1899,
                            "chrUn_KI270528v1":2983,
                            "chrUn_KI270530v1":2168,
                            "chrUn_KI270539v1":993,
                            "chrUn_KI270538v1":91309,
                            "chrUn_KI270544v1":1202,
                            "chrUn_KI270548v1":1599,
                            "chrUn_KI270583v1":1400,
                            "chrUn_KI270587v1":2969,
                            "chrUn_KI270580v1":1553,
                            "chrUn_KI270581v1":7046,
                            "chrUn_KI270579v1":31033,
                            "chrUn_KI270589v1":44474,
                            "chrUn_KI270590v1":4685,
                            "chrUn_KI270584v1":4513,
                            "chrUn_KI270582v1":6504,
                            "chrUn_KI270588v1":6158,
                            "chrUn_KI270593v1":3041,
                            "chrUn_KI270591v1":5796,
                            "chrUn_KI270330v1":1652,
                            "chrUn_KI270329v1":1040,
                            "chrUn_KI270334v1":1368,
                            "chrUn_KI270333v1":2699,
                            "chrUn_KI270335v1":1048,
                            "chrUn_KI270338v1":1428,
                            "chrUn_KI270340v1":1428,
                            "chrUn_KI270336v1":1026,
                            "chrUn_KI270337v1":1121,
                            "chrUn_KI270363v1":1803,
                            "chrUn_KI270364v1":2855,
                            "chrUn_KI270362v1":3530,
                            "chrUn_KI270366v1":8320,
                            "chrUn_KI270378v1":1048,
                            "chrUn_KI270379v1":1045,
                            "chrUn_KI270389v1":1298,
                            "chrUn_KI270390v1":2387,
                            "chrUn_KI270387v1":1537,
                            "chrUn_KI270395v1":1143,
                            "chrUn_KI270396v1":1880,
                            "chrUn_KI270388v1":1216,
                            "chrUn_KI270394v1":970,
                            "chrUn_KI270386v1":1788,
                            "chrUn_KI270391v1":1484,
                            "chrUn_KI270383v1":1750,
                            "chrUn_KI270393v1":1308,
                            "chrUn_KI270384v1":1658,
                            "chrUn_KI270392v1":971,
                            "chrUn_KI270381v1":1930,
                            "chrUn_KI270385v1":990,
                            "chrUn_KI270382v1":4215,
                            "chrUn_KI270376v1":1136,
                            "chrUn_KI270374v1":2656,
                            "chrUn_KI270372v1":1650,
                            "chrUn_KI270373v1":1451,
                            "chrUn_KI270375v1":2378,
                            "chrUn_KI270371v1":2805,
                            "chrUn_KI270448v1":7992,
                            "chrUn_KI270521v1":7642,
                            "chrUn_GL000195v1":182896,
                            "chrUn_GL000219v1":179198,
                            "chrUn_GL000220v1":161802,
                            "chrUn_GL000224v1":179693,
                            "chrUn_KI270741v1":157432,
                            "chrUn_GL000226v1":15008,
                            "chrUn_GL000213v1":164239,
                            "chrUn_KI270743v1":210658,
                            "chrUn_KI270744v1":168472,
                            "chrUn_KI270745v1":41891,
                            "chrUn_KI270746v1":66486,
                            "chrUn_KI270747v1":198735,
                            "chrUn_KI270748v1":93321,
                            "chrUn_KI270749v1":158759,
                            "chrUn_KI270750v1":148850,
                            "chrUn_KI270751v1":150742,
                            "chrUn_KI270752v1":27745,
                            "chrUn_KI270753v1":62944,
                            "chrUn_KI270754v1":40191,
                            "chrUn_KI270755v1":36723,
                            "chrUn_KI270756v1":79590,
                            "chrUn_KI270757v1":71251,
                            "chrUn_GL000214v1":137718,
                            "chrUn_KI270742v1":186739,
                            "chrUn_GL000216v2":176608,
                            "chrUn_GL000218v1":161147,
                            "chr1_KI270762v1_alt":354444,
                            "chr1_KI270766v1_alt":256271,
                            "chr1_KI270760v1_alt":109528,
                            "chr1_KI270765v1_alt":185285,
                            "chr1_GL383518v1_alt":182439,
                            "chr1_GL383519v1_alt":110268,
                            "chr1_GL383520v2_alt":366580,
                            "chr1_KI270764v1_alt":50258,
                            "chr1_KI270763v1_alt":911658,
                            "chr1_KI270759v1_alt":425601,
                            "chr1_KI270761v1_alt":165834,
                            "chr2_KI270770v1_alt":136240,
                            "chr2_KI270773v1_alt":70887,
                            "chr2_KI270774v1_alt":223625,
                            "chr2_KI270769v1_alt":120616,
                            "chr2_GL383521v1_alt":143390,
                            "chr2_KI270772v1_alt":133041,
                            "chr2_KI270775v1_alt":138019,
                            "chr2_KI270771v1_alt":110395,
                            "chr2_KI270768v1_alt":110099,
                            "chr2_GL582966v2_alt":96131,
                            "chr2_GL383522v1_alt":123821,
                            "chr2_KI270776v1_alt":174166,
                            "chr2_KI270767v1_alt":161578,
                            "chr3_JH636055v2_alt":173151,
                            "chr3_KI270783v1_alt":109187,
                            "chr3_KI270780v1_alt":224108,
                            "chr3_GL383526v1_alt":180671,
                            "chr3_KI270777v1_alt":173649,
                            "chr3_KI270778v1_alt":248252,
                            "chr3_KI270781v1_alt":113034,
                            "chr3_KI270779v1_alt":205312,
                            "chr3_KI270782v1_alt":162429,
                            "chr3_KI270784v1_alt":184404,
                            "chr4_KI270790v1_alt":220246,
                            "chr4_GL383528v1_alt":376187,
                            "chr4_KI270787v1_alt":111943,
                            "chr4_GL000257v2_alt":586476,
                            "chr4_KI270788v1_alt":158965,
                            "chr4_GL383527v1_alt":164536,
                            "chr4_KI270785v1_alt":119912,
                            "chr4_KI270789v1_alt":205944,
                            "chr4_KI270786v1_alt":244096,
                            "chr5_KI270793v1_alt":126136,
                            "chr5_KI270792v1_alt":179043,
                            "chr5_KI270791v1_alt":195710,
                            "chr5_GL383532v1_alt":82728,
                            "chr5_GL949742v1_alt":226852,
                            "chr5_KI270794v1_alt":164558,
                            "chr5_GL339449v2_alt":1612928,
                            "chr5_GL383530v1_alt":101241,
                            "chr5_KI270796v1_alt":172708,
                            "chr5_GL383531v1_alt":173459,
                            "chr5_KI270795v1_alt":131892,
                            "chr6_GL000250v2_alt":4672374,
                            "chr6_KI270800v1_alt":175808,
                            "chr6_KI270799v1_alt":152148,
                            "chr6_GL383533v1_alt":124736,
                            "chr6_KI270801v1_alt":870480,
                            "chr6_KI270802v1_alt":75005,
                            "chr6_KB021644v2_alt":185823,
                            "chr6_KI270797v1_alt":197536,
                            "chr6_KI270798v1_alt":271782,
                            "chr7_KI270804v1_alt":157952,
                            "chr7_KI270809v1_alt":209586,
                            "chr7_KI270806v1_alt":158166,
                            "chr7_GL383534v2_alt":119183,
                            "chr7_KI270803v1_alt":1111570,
                            "chr7_KI270808v1_alt":271455,
                            "chr7_KI270807v1_alt":126434,
                            "chr7_KI270805v1_alt":209988,
                            "chr8_KI270818v1_alt":145606,
                            "chr8_KI270812v1_alt":282736,
                            "chr8_KI270811v1_alt":292436,
                            "chr8_KI270821v1_alt":985506,
                            "chr8_KI270813v1_alt":300230,
                            "chr8_KI270822v1_alt":624492,
                            "chr8_KI270814v1_alt":141812,
                            "chr8_KI270810v1_alt":374415,
                            "chr8_KI270819v1_alt":133535,
                            "chr8_KI270820v1_alt":36640,
                            "chr8_KI270817v1_alt":158983,
                            "chr8_KI270816v1_alt":305841,
                            "chr8_KI270815v1_alt":132244,
                            "chr9_GL383539v1_alt":162988,
                            "chr9_GL383540v1_alt":71551,
                            "chr9_GL383541v1_alt":171286,
                            "chr9_GL383542v1_alt":60032,
                            "chr9_KI270823v1_alt":439082,
                            "chr10_GL383545v1_alt":179254,
                            "chr10_KI270824v1_alt":181496,
                            "chr10_GL383546v1_alt":309802,
                            "chr10_KI270825v1_alt":188315,
                            "chr11_KI270832v1_alt":210133,
                            "chr11_KI270830v1_alt":177092,
                            "chr11_KI270831v1_alt":296895,
                            "chr11_KI270829v1_alt":204059,
                            "chr11_GL383547v1_alt":154407,
                            "chr11_JH159136v1_alt":200998,
                            "chr11_JH159137v1_alt":191409,
                            "chr11_KI270827v1_alt":67707,
                            "chr11_KI270826v1_alt":186169,
                            "chr12_GL877875v1_alt":167313,
                            "chr12_GL877876v1_alt":408271,
                            "chr12_KI270837v1_alt":40090,
                            "chr12_GL383549v1_alt":120804,
                            "chr12_KI270835v1_alt":238139,
                            "chr12_GL383550v2_alt":169178,
                            "chr12_GL383552v1_alt":138655,
                            "chr12_GL383553v2_alt":152874,
                            "chr12_KI270834v1_alt":119498,
                            "chr12_GL383551v1_alt":184319,
                            "chr12_KI270833v1_alt":76061,
                            "chr12_KI270836v1_alt":56134,
                            "chr13_KI270840v1_alt":191684,
                            "chr13_KI270839v1_alt":180306,
                            "chr13_KI270843v1_alt":103832,
                            "chr13_KI270841v1_alt":169134,
                            "chr13_KI270838v1_alt":306913,
                            "chr13_KI270842v1_alt":37287,
                            "chr14_KI270844v1_alt":322166,
                            "chr14_KI270847v1_alt":1511111,
                            "chr14_KI270845v1_alt":180703,
                            "chr14_KI270846v1_alt":1351393,
                            "chr15_KI270852v1_alt":478999,
                            "chr15_KI270851v1_alt":263054,
                            "chr15_KI270848v1_alt":327382,
                            "chr15_GL383554v1_alt":296527,
                            "chr15_KI270849v1_alt":244917,
                            "chr15_GL383555v2_alt":388773,
                            "chr15_KI270850v1_alt":430880,
                            "chr16_KI270854v1_alt":134193,
                            "chr16_KI270856v1_alt":63982,
                            "chr16_KI270855v1_alt":232857,
                            "chr16_KI270853v1_alt":2659700,
                            "chr16_GL383556v1_alt":192462,
                            "chr16_GL383557v1_alt":89672,
                            "chr17_GL383563v3_alt":375691,
                            "chr17_KI270862v1_alt":391357,
                            "chr17_KI270861v1_alt":196688,
                            "chr17_KI270857v1_alt":2877074,
                            "chr17_JH159146v1_alt":278131,
                            "chr17_JH159147v1_alt":70345,
                            "chr17_GL383564v2_alt":133151,
                            "chr17_GL000258v2_alt":1821992,
                            "chr17_GL383565v1_alt":223995,
                            "chr17_KI270858v1_alt":235827,
                            "chr17_KI270859v1_alt":108763,
                            "chr17_GL383566v1_alt":90219,
                            "chr17_KI270860v1_alt":178921,
                            "chr18_KI270864v1_alt":111737,
                            "chr18_GL383567v1_alt":289831,
                            "chr18_GL383570v1_alt":164789,
                            "chr18_GL383571v1_alt":198278,
                            "chr18_GL383568v1_alt":104552,
                            "chr18_GL383569v1_alt":167950,
                            "chr18_GL383572v1_alt":159547,
                            "chr18_KI270863v1_alt":167999,
                            "chr19_KI270868v1_alt":61734,
                            "chr19_KI270865v1_alt":52969,
                            "chr19_GL383573v1_alt":385657,
                            "chr19_GL383575v2_alt":170222,
                            "chr19_GL383576v1_alt":188024,
                            "chr19_GL383574v1_alt":155864,
                            "chr19_KI270866v1_alt":43156,
                            "chr19_KI270867v1_alt":233762,
                            "chr19_GL949746v1_alt":987716,
                            "chr20_GL383577v2_alt":128386,
                            "chr20_KI270869v1_alt":118774,
                            "chr20_KI270871v1_alt":58661,
                            "chr20_KI270870v1_alt":183433,
                            "chr21_GL383578v2_alt":63917,
                            "chr21_KI270874v1_alt":166743,
                            "chr21_KI270873v1_alt":143900,
                            "chr21_GL383579v2_alt":201197,
                            "chr21_GL383580v2_alt":74653,
                            "chr21_GL383581v2_alt":116689,
                            "chr21_KI270872v1_alt":82692,
                            "chr22_KI270875v1_alt":259914,
                            "chr22_KI270878v1_alt":186262,
                            "chr22_KI270879v1_alt":304135,
                            "chr22_KI270876v1_alt":263666,
                            "chr22_KI270877v1_alt":101331,
                            "chr22_GL383583v2_alt":96924,
                            "chr22_GL383582v2_alt":162811,
                            "chrX_KI270880v1_alt":284869,
                            "chrX_KI270881v1_alt":144206,
                            "chr19_KI270882v1_alt":248807,
                            "chr19_KI270883v1_alt":170399,
                            "chr19_KI270884v1_alt":157053,
                            "chr19_KI270885v1_alt":171027,
                            "chr19_KI270886v1_alt":204239,
                            "chr19_KI270887v1_alt":209512,
                            "chr19_KI270888v1_alt":155532,
                            "chr19_KI270889v1_alt":170698,
                            "chr19_KI270890v1_alt":184499,
                            "chr19_KI270891v1_alt":170680,
                            "chr1_KI270892v1_alt":162212,
                            "chr2_KI270894v1_alt":214158,
                            "chr2_KI270893v1_alt":161218,
                            "chr3_KI270895v1_alt":162896,
                            "chr4_KI270896v1_alt":378547,
                            "chr5_KI270897v1_alt":1144418,
                            "chr5_KI270898v1_alt":130957,
                            "chr6_GL000251v2_alt":4795265,
                            "chr7_KI270899v1_alt":190869,
                            "chr8_KI270901v1_alt":136959,
                            "chr8_KI270900v1_alt":318687,
                            "chr11_KI270902v1_alt":106711,
                            "chr11_KI270903v1_alt":214625,
                            "chr12_KI270904v1_alt":572349,
                            "chr15_KI270906v1_alt":196384,
                            "chr15_KI270905v1_alt":5161414,
                            "chr17_KI270907v1_alt":137721,
                            "chr17_KI270910v1_alt":157099,
                            "chr17_KI270909v1_alt":325800,
                            "chr17_JH159148v1_alt":88070,
                            "chr17_KI270908v1_alt":1423190,
                            "chr18_KI270912v1_alt":174061,
                            "chr18_KI270911v1_alt":157710,
                            "chr19_GL949747v2_alt":729520,
                            "chr22_KB663609v1_alt":74013,
                            "chrX_KI270913v1_alt":274009,
                            "chr19_KI270914v1_alt":205194,
                            "chr19_KI270915v1_alt":170665,
                            "chr19_KI270916v1_alt":184516,
                            "chr19_KI270917v1_alt":190932,
                            "chr19_KI270918v1_alt":123111,
                            "chr19_KI270919v1_alt":170701,
                            "chr19_KI270920v1_alt":198005,
                            "chr19_KI270921v1_alt":282224,
                            "chr19_KI270922v1_alt":187935,
                            "chr19_KI270923v1_alt":189352,
                            "chr3_KI270924v1_alt":166540,
                            "chr4_KI270925v1_alt":555799,
                            "chr6_GL000252v2_alt":4604811,
                            "chr8_KI270926v1_alt":229282,
                            "chr11_KI270927v1_alt":218612,
                            "chr19_GL949748v2_alt":1064304,
                            "chr22_KI270928v1_alt":176103,
                            "chr19_KI270929v1_alt":186203,
                            "chr19_KI270930v1_alt":200773,
                            "chr19_KI270931v1_alt":170148,
                            "chr19_KI270932v1_alt":215732,
                            "chr19_KI270933v1_alt":170537,
                            "chr19_GL000209v2_alt":177381,
                            "chr3_KI270934v1_alt":163458,
                            "chr6_GL000253v2_alt":4677643,
                            "chr19_GL949749v2_alt":1091841,
                            "chr3_KI270935v1_alt":197351,
                            "chr6_GL000254v2_alt":4827813,
                            "chr19_GL949750v2_alt":1066390,
                            "chr3_KI270936v1_alt":164170,
                            "chr6_GL000255v2_alt":4606388,
                            "chr19_GL949751v2_alt":1002683,
                            "chr3_KI270937v1_alt":165607,
                            "chr6_GL000256v2_alt":4929269,
                            "chr19_GL949752v1_alt":987100,
                            "chr6_KI270758v1_alt":76752,
                            "chr19_GL949753v2_alt":796479,
                            "chr19_KI270938v1_alt":1066800,
                            "chrEBV":171823}

        self.chromosomes = np.array(list(self.chrom_sizes.keys()))

        self.main_chromosomes = np.array(["chr1","chr2","chr3","chr4","chr5","chr6","chr7",
                                        "chr8","chr9","chr10","chr11","chr12","chr13",
                                        "chr14","chr15","chr16","chr17","chr18","chr19",
                                        "chr20","chr21","chr22","chrX","chrY","chrM"])

        self.autosomes = np.array(["chr1","chr2","chr3","chr4","chr5","chr6","chr7",
                                    "chr8","chr9","chr10","chr11","chr12","chr13",
                                    "chr14","chr15","chr16","chr17","chr18","chr19",
                                    "chr20","chr21","chr22"])


    def exons(self,
              chromosome: str = None,
              upstream: int = 0,
              downstream: int = 0) -> IntervalFrame:
        """
        Exons

        Parameters
        ----------
            chromosome : str
                Chromosome name
            upstream : int
                Upstream distance
            downstream : int
                Downstream distance
        
        Returns
        -------
            features : IntervalFrame
                Exons

        """

        features = get_exons(chromosome=chromosome,
                            upstream=upstream,
                            downstream=downstream)

        return features


    def tss(self,
            chromosome: str = None,
            upstream: int = 0,
            downstream: int = 0,
            gene_type: str = "all",
            filter_duplicates: bool = True) -> IntervalFrame:
        """
        """

        return get_tss(chromosome=chromosome,
                       upstream=upstream,
                       downstream=downstream,
                       gene_type=gene_type,
                       filter_duplicates=filter_duplicates)
    
    def tes(self,
            chromosome: str = None,
            upstream: int = 0,
            downstream: int = 0,
            filter_duplicates: bool = True) -> IntervalFrame:
        """
        """

        return get_tes(chromosome=chromosome,
                       upstream=upstream,
                       downstream=downstream,
                       filter_duplicates=filter_duplicates)

    
    def cpg_islands(self,
                    chromosome: str = None,
                    upstream: int = 0,
                    downstream: int = 0) -> IntervalFrame:
        """
        """

        raise NotImplementedError("Feature not implemented yet.")

        return get_cpg_islands(chromosome=chromosome,
                               upstream=upstream,
                               downstream=downstream)


    def genes(self,
              chromosome: str = None,
              upstream: int = 0,
              downstream: int = 0,
              gene_type: int = "all") -> IntervalFrame:
        """
        """

        return get_gene_body(chromosome=chromosome,
                             upstream=upstream,
                             downstream=downstream,
                             gene_type=gene_type)

    def tfbs(self,
             chromosome: str = None,
             upstream: int = 0,
             downstream: int = 0) -> IntervalFrame:
        """
        """

        raise NotImplementedError("Feature not implemented yet.")

        return get_tfbs(chromosome, upstream, downstream)


    def ctcf(self,
            chromosome: str = None,
            upstream: int = 0,
            downstream: int = 0) -> IntervalFrame:
        """
        """

        raise NotImplementedError("Feature not implemented yet.")
        
        return get_ctcf(chromosome, upstream, downstream)

    
    def bin_bias(self,
                 bin_size: int = 100000) -> IntervalFrame:
        """
        """
        
        bias = get_bin_bias(bin_size)
        
        return bias
    

    def blacklist(self) -> IntervalFrame:
        """
        """
        
        return get_blacklist()


    def repeats(self) -> IntervalFrame:
        """
        """

        raise NotImplementedError("Feature not implemented yet.")
        
        return get_repeats()


    def kmers(self,
              intervals: LabeledIntervalArray,
              k: int = 2,
              last_n: int = 0) -> IntervalFrame:
        """
        """

        return interval_kmers(intervals, k, last_n)

    
    def sequence(self,
                chromosome: str,
                start: int,
                end: int) -> str:
        """
        """

        return get_sequence(chromosome, start, end)

    
    def CpGs(self,
             chromosome: str = None,
             upstream: int = 0,
             downstream: int = 0) -> IntervalFrame:
        """
        """

        raise NotImplementedError("Feature not implemented yet.")

        cpgs = get_cpgs(chromosome, upstream, downstream)

        return cpgs


    def CpG_names(self) -> np.ndarray:
        """
        """

        raise NotImplementedError("Feature not implemented yet.")

        cpgs = get_cpg_names()

        return cpgs


    @property
    def reference_file(self):
        """
        """

        return  get_data_file("hg38.2bit")

    @property
    def reference_cpgs_file(self):
        """
        """

        raise NotImplementedError("Feature not implemented yet.")

        return get_data_file("hg38_CpGs.h5")