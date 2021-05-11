def ansysSignalLine_Lines(node):
    return ["oModuleBoundary.AssignSignalNet(\n",\
        "    [\n",\
        "        \"NAME:"+node.name+"\",\n",\
        "        \"Objects:=\"		, [\""+node.name+"\"]\n",\
        "    ])\n"]
def netlistHeaderLines():#Not currently a function of simulation. Not sure if it will ever need to be. 
        return [".option PARHIER=\'local\'\n",\
               ".option max_messages=1\n",\
               ".option num_threads=4\n"]
def ansysSaveLine():
    return "oProject.Save()\n"
def ansysUniteNodes(nodeList):
    insertionLine=nodeList[0].name+","
    for thisNode in nodeList[1:-1]:
        insertionLine=insertionLine+thisNode.name+","
    insertionLine=insertionLine+nodeList[-1].name
    return ["oEditor.Unite(\n",\
            "    [\n",\
            "        \"NAME:Selections\",\n",\
            "        \"Selections:=\"		, \""+insertionLine+"\"\n",\
            "    ],\n",\
            "    [\n",\
            "        \"NAME:UniteParameters\",\n",\
            "        \"KeepOriginals:=\"	, False\n",\
            "    ])\n"]
def aedtEdit(line):#This function edits the aedt file lines to add a backslash before each single quote. Needed for loading in the netlist
    returnLine=""
    for char in line:
        if char=="\'":
            returnLine=returnLine+"\\"+char
        else:
            returnLine=returnLine+char        
    return returnLine
def netlistSimulationLines(simType,simParams):#Contains simulation-specific info
    if simType=="fullS21" or\
       simType[0:9]=="circFreqQ" or\
       simType[0:9]=="circFreqR" or\
       simType[0:7]=="lumpedR" or\
       simType[0:11]=="freqLumpedR" or\
       simType[0:6]=="decayQ" or\
       simType[0:5]=="exchQ" or\
       simType[0:17]=="feedlineCouplingR":
       
       return [".LNA\n",\
               "+ LIN "+str(simParams["LNA_counts"])+" "+str(simParams["LNA_start (GHz)"]*1e9)+" "+str(simParams["LNA_stop (GHz)"]*1e9)+"\n",\
               "+ FLAG=\'LNA\'\n"] 
def ansysOutputToComplex(complexString):
    return complexString.replace("i","j").replace(" ","")