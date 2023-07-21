#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Exchange

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""
from ArticutAPI import Articut
from random import sample
import json
import os


DEBUG_Exchange = True
CHATBOT_MODE = False

try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_Exchange.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Exchange:
        print("[Exchange] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    
    if utterance == "[100元][日幣]換[美金]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["source"] = args[1]
            resultDICT["target"] = args[2]
            resultDICT["amount"] = args[0]
            pass

    if utterance == "[100台幣]換[日幣]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['source'] = args[0]
            resultDICT['target'] = args[1]
            resultDICT['amount'] = None
            pass

    if utterance == "[台幣][100]換[美金]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['source'] = args[0]
            resultDICT['target'] = args[2]
            resultDICT['amount'] = args[1]    
            pass

    if utterance == "[台幣]換[100元][美金]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT['source'] = args[0]
            resultDICT['target'] = args[2]
            resultDICT['amount'] = args[1]
            pass

    if utterance == "[台幣]換[100美金]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["source"] = args[0]
            resultDICT["target"] = None
            resultDICT["amount"] = args[1]
            pass

    if utterance == "[台幣]換[美金][100]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["source"] = args[0]
            resultDICT["target"] = args[1]
            resultDICT["amount"] = args[2]
            pass

    return resultDICT