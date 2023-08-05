import pandas as pd
import numpy as np

from k3cloud_webapi_sdk.main import K3CloudApiSdk

api_sdk = K3CloudApiSdk()

api_sdk.InitConfig('62f49d037697ee', '张志', '232255_1eeC0aDJ1rGaSexHx1wrz/9tzNQZ1okE',
                   '1bb7607d115547b3b153c43959f054ee', 'http://cellprobio.gnway.cc/k3cloud')

def save(formid,data):
    for i in data.index:
        if str(data.loc[i]["物料编码"])!="":
            model={
                "Model": {
                    "FMATERIALID": 0,
                    "FCreateOrgId": {
                        "FNumber": "100"
                    },
                    "FUseOrgId": {
                        "FNumber": "100"
                    },
                    "FNumber": str(data.loc[i]["物料编码"]),
                    "FName": str(data.loc[i]["物料名称"]),
                    "FSpecification": str(data.loc[i]["规格型号"]),
                    "FDescription": str(data.loc[i]["物料描述"]),
                    "FMaterialGroup": {
                        "FNumber": str(data.loc[i]["物料分组"])
                    },
                    "FDSMatchByLot": False,
                    "FImgStorageType": "A",
                    "FIsSalseByNet": False,
                    "F_SZSP_Decimal": 1.0,
                    "F_SZSP_Decimal1": 1.0,
                    "FSubHeadEntity": {
                        "FIsControlSal": False,
                        "FIsAutoRemove": False,
                        "FIsMailVirtual": False,
                        "FTimeUnit": "H",
                        "FIsPrinttAg": False,
                        "FIsAccessory": False
                    },
                    "SubHeadEntity": {
                        "FErpClsID":  str(data.loc[i]["物料属性"]),
                        "FFeatureItem": "1",
                        "FCategoryID": {
                            "FNumber": str(data.loc[i]["存货类别"])
                        },
                        "FTaxType": {
                            "FNumber": "WLDSFL01_SYS"
                        },
                        "FTaxRateId": {
                            "FNUMBER": str(data.loc[i]["默认税率%"])
                        },
                        "FBaseUnitId": {
                            "FNumber": str(data.loc[i]["基本单位"])
                            # "FNumber": "01"
                        },
                        # "FIsPurchase": True,
                        # "FIsInventory": True,
                        # "FIsSubContract": False,
                        # "FIsSale": True,
                        # "FIsProduce": False,
                        # "FIsAsset": False,
                        "FGROSSWEIGHT":  str(data.loc[i]["毛重"]),
                        "FNETWEIGHT": str(data.loc[i]["净重"]),
                        "FWEIGHTUNITID": {
                            "FNUMBER": str(data.loc[i]["重量单位"])
                        },
                        # "FOrderPolicy": str(data.loc[i]["订货策略"]),
                        "FLENGTH": str(data.loc[i]["长"]),
                        "FWIDTH": str(data.loc[i]["宽"]),
                        "FHEIGHT": str(data.loc[i]["高"]),
                        "FVOLUME": str(data.loc[i]["体积"]),
                        "FVOLUMEUNITID": {
                            "FNUMBER": str(data.loc[i]["尺寸单位"])
                        }
                    },
                    "SubHeadEntity1": {
                        "FStoreUnitID": {
                            "FNumber": str(data.loc[i]["基本单位"])
                        },
                        "FUnitConvertDir": "1",
                        "FIsLockStock": True,
                        "FIsCycleCounting": False,
                        "FCountCycle": "1",
                        "FCountDay": 1,
                        "FIsMustCounting": False,
                        "FIsBatchManage": str(data.loc[i]["启用批号管理"]),
                        "FIsKFPeriod": False,
                        "FIsExpParToFlot": False,
                        "FCurrencyId": {
                            "FNumber": "PRE001"
                        },
                        "FIsEnableMinStock": False,
                        "FIsEnableMaxStock": False,
                        "FIsEnableSafeStock": True,
                        "FIsEnableReOrder": False,
                        "FSafeStock": str(data.loc[i]["安全库存"]),
                        "FIsSNManage": False,
                        "FIsSNPRDTracy": False,
                        "FSNManageType": "1",
                        "FSNGenerateTime": "1"
                    },
                    "FTaxCategoryCodeId": {
                        "FNUMBER": str(data.loc[i]["税收分类"])
                    },
                    # "FOrderIntervalTime": "3",
                    "SubHeadEntity2": {
                        "FSaleUnitId": {
                            "FNumber": str(data.loc[i]["基本单位"])
                        },
                        "FSalePriceUnitId": {
                            "FNumber": str(data.loc[i]["基本单位"])
                        },
                        "FMaxQty": 100000.0,
                        "FIsATPCheck": False,
                        "FIsReturnPart": False,
                        "FIsInvoice": False,
                        "FIsReturn": True,
                        "FAllowPublish": False,
                        "FISAFTERSALE": True,
                        "FISPRODUCTFILES": True,
                        "FISWARRANTED": False,
                        "FWARRANTYUNITID": "D",
                        "FOutLmtUnit": "SAL",
                        "FIsTaxEnjoy": False,
                        "FUnValidateExpQty": False
                    },
                    "SubHeadEntity3": {
                        "FPurchaseUnitId": {
                            "FNumber": str(data.loc[i]["基本单位"])
                        },
                        "FPurchasePriceUnitId": {
                            "FNumber": str(data.loc[i]["基本单位"])
                        },
                        "FIsQuota": False,
                        "FQuotaType": "1",
                        "FIsVmiBusiness": False,
                        "FEnableSL": False,
                        "FIsPR": False,
                        "FIsReturnMaterial": True,
                        "FIsSourceControl": False,
                        "FPOBillTypeId": {
                            "FNUMBER": "CGSQD01_SYS"
                        },
                        "FPrintCount": 1,
                        "FMinPackCount": str(data.loc[i]["最小包装数"])
                    },
                    "SubHeadEntity4": {
                        "FPlanningStrategy": str(data.loc[i]["计划策略"]),
                        "FMfgPolicyId": {
                            "FNumber": "ZZCL001_SYS"
                        },
                        "FFixLeadTime": str(data.loc[i]["固定提前期"]),
                        "FFixLeadTimeType": "1",
                        "FVarLeadTime": str(data.loc[i]["变动提前期"]),
                        "FVarLeadTimeType": "1",
                        "FCheckLeadTimeType": "1",
                        "FOrderIntervalTimeType": "3",
                        "FMaxPOQty": str(data.loc[i]["最大订货量"]),
                        "FMinPOQty": str(data.loc[i]["最小订货量"]),
                        "FIncreaseQty": str(data.loc[i]["最小包装量"]),
                        "FEOQ": str(data.loc[i]["固定/经济批量"]),
                        "FVarLeadTimeLotSize": str(data.loc[i]["变动提前期批量"]),
                        "FIsMrpComBill": True,
                        "FIsMrpComReq": False,
                        "FReserveType": "1",
                        "FPlanSafeStockQty": 100.0,
                        "FAllowPartAhead": False,
                        "FCanDelayDays": 999,
                        "FAllowPartDelay": True,
                        "FPlanOffsetTimeType": "1",
                        "FWriteOffQty": 1.0
                    },
                    "SubHeadEntity5": {
                        "FProduceUnitId": {
                            "FNumber": str(data.loc[i]["基本单位"])
                        },
                        "FProduceBillType": {
                            "FNUMBER": "SCDD01_SYS"
                        },
                        "FIsSNCarryToParent": False,
                        "FIsProductLine": False,
                        "FBOMUnitId": {
                            "FNumber": str(data.loc[i]["基本单位"])
                        },
                        "FIsMainPrd": False,
                        "FIsCoby": False,
                        "FIsECN": False,
                        "FIssueType": "1",
                        "FOverControlMode": str(data.loc[i]["超发控制方式"]),
                        "FMinIssueQty": str(data.loc[i]["最小发料批量"]),
                        "FISMinIssueQty": str(data.loc[i]["领料考虑最小发料批量"]),
                        "FIsKitting": False,
                        "FIsCompleteSet": False,
                        "FMinIssueUnitId": {
                            "FNUMBER": str(data.loc[i]["基本单位"])
                        },
                        "FStandHourUnitId": "3600",
                        "FBackFlushType": "1",
                        "FIsEnableSchedule": False
                    },
                    "SubHeadEntity7": {
                        "FSubconUnitId": {
                            "FNumber": str(data.loc[i]["基本单位"])
                        },
                        "FSubconPriceUnitId": {
                            "FNumber": str(data.loc[i]["基本单位"])
                        }
                    },
                    "SubHeadEntity6": {
                        "FCheckIncoming": False,
                        "FCheckProduct": False,
                        "FCheckStock": False,
                        "FCheckReturn": False,
                        "FCheckDelivery": False,
                        "FEnableCyclistQCSTK": False,
                        "FEnableCyclistQCSTKEW": False,
                        "FCheckEntrusted": False,
                        "FCheckOther": False,
                        "FIsFirstInspect": False,
                        "FCheckReturnMtrl": False
                    },
                    "FEntityInvPty": [
                        {
                            "FInvPtyId": {
                                "FNumber": "01"
                            },
                            "FIsEnable": True,
                            "FIsAffectPrice": False,
                            "FIsAffectPlan": False,
                            "FIsAffectCost": False
                        },
                        {
                            "FInvPtyId": {
                                "FNumber": "02"
                            },
                            "FIsEnable": True,
                            "FIsAffectPrice": False,
                            "FIsAffectPlan": False,
                            "FIsAffectCost": False
                        },
                        {
                            "FInvPtyId": {
                                "FNumber": "03"
                            },
                            "FIsEnable": False,
                            "FIsAffectPrice": False,
                            "FIsAffectPlan": False,
                            "FIsAffectCost": False
                        },
                        {
                            "FInvPtyId": {
                                "FNumber": "04"
                            },
                            "FIsEnable": False,
                            "FIsAffectPrice": False,
                            "FIsAffectPlan": False,
                            "FIsAffectCost": False
                        },
                        {
                            "FInvPtyId": {
                                "FNumber": "06"
                            },
                            "FIsEnable": False,
                            "FIsAffectPrice": False,
                            "FIsAffectPlan": False,
                            "FIsAffectCost": False
                        }
                    ]
                }
            }
            res=api_sdk.Save(formid,model)
            print(res)



# def dataPreprocess(data,path,Material,):
#     resource = pd.read_excel(path)
#
#     resource = resource.fillna("")
#
#     transformData = pd.read_excel(path, Material)
#
#     transformData = transformData.set_index('key').to_dict()
#
#     x = 0
#
#     for i in resource[Material]:
#         resource.loc[x, Material] = transformData["value"][i]
#         x += 1
#
#     res = resource
#
#     return res



def dataPreprocess(data,Cpath):
    data1 = pd.read_excel(Cpath)
    data1 = np.array(data1)
    d1 = dict(data1)

    data2 = pd.read_excel(Cpath,"基本单位")
    data2 = np.array(data2)
    d2 = dict(data2)

    data3 = pd.read_excel(Cpath, "物料属性")
    data3 = np.array(data3)
    d3 = dict(data3)

    data4 = pd.read_excel(Cpath, "产品大类")
    data4 = np.array(data4)
    d4 = dict(data4)

    data5 = pd.read_excel(Cpath, "默认税率")
    data5 = np.array(data5)
    d5 = dict(data5)

    # print(d2)

    x = 0

    for i in data["存货类别"]:
        if i=="":
            pass
        else:
            data.loc[x,"存货类别"]=d1[i]
            x += 1

    a = 0

    for i in data["基本单位"]:

        if i=="":
            data.loc[a, "基本单位"] ="Pcs"
        else:
            data.loc[a, "基本单位"] = d2[i]

        a += 1

    b = 0

    for i in data["物料属性"]:
        if i=="":
            pass
        else:

            data.loc[b, "物料属性"] = d3[i]

            b += 1

    c = 0

    for i in data["重量单位"]:
        if i=="":
            data.loc[c, "重量单位"] ="kg"
        else:
            data.loc[c, "重量单位"] = d2[i]

        c += 1

    d = 0

    for i in data["尺寸单位"]:
        if i=="":
            data.loc[d, "尺寸单位"] = "m"
        else:
            data.loc[d, "尺寸单位"] = d2[i]
        d += 1

    e = 0

    for i in data["产品大类"]:
        if i == "":
            data.loc[e, "产品大类"] = ""
        else:
            data.loc[e, "产品大类"] = d4[i]
        e += 1

    f = 0

    for i in data["默认税率%"]:
        if i == "":
            data.loc[f, "默认税率%"] = "SL02_SYS"
        else:
            data.loc[f, "默认税率%"] = d5[i]
        f += 1

    # c = 0

    # for i in data["重量单位"]:
    #     data.loc[c, "重量单位"] = d2[i]
    #
    #     c += 1


    return data

def handleNum(resource):
    '''

    :param resource:
    :return:
    '''
    a = 0
    for k in resource["固定/经济批量"]:
        if k == "":
            resource.loc[a, "固定/经济批量"] = 1

        a += 1

    b = 0
    for k in resource["变动提前期批量"]:
        if k == "":
            resource.loc[b, "变动提前期批量"] = 1

        b += 1

    c = 0
    for k in resource["最小发料批量"]:
        if k == "":
            resource.loc[c, "最小发料批量"] = 1

        c += 1
    res=resource

    return res


def saveData(path):
    resource = pd.read_excel(path)

    resource = resource.fillna("")

    resource = resource.replace("否", False)
    resource = resource.replace("是", True)

    data = dataPreprocess(resource)

    result = handleNum(data)

    save("BD_MATERIAL", result)




if __name__ == '__main__':
    resource = pd.read_excel("D:\物料-2022-8-18(1).xlsx")

    resource=resource.fillna("")

    resource = resource.replace("否", False)
    resource = resource.replace("是", True)

    data=dataPreprocess(resource)

    result=handleNum(data)

    # print(result)

    # print(save("BD_MATERIAL",result))

    save("BD_MATERIAL", result)

    # for i in result["重量单位"]:
    #     print(i)


    # for i in result["默认税率%"]:
    #     print(i)

