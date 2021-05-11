import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Y11Q1")
oDesign = oProject.SetActiveDesign("Netlist")
oModuleReport = oDesign.GetModule("ReportSetup")
oDesign.AnalyzeAll()
oModuleReport.CreateReport("Y Parameter Table 1", "Standard", "Data Table", "LNA",
    [
        "NAME:Context",
        "SimValueContext:="	, [3,0,2,0,False,False,-1,1,0,1,1,"",0,0]
    ],
    [
        "F:="			, ["All"]
    ],
    [
        "X Component:="		, "F",
        "Y Component:="		, ["Y(1,1)"]
    ], [])
oModuleReport.ExportToFile("Y Parameter Table 1", "O:/68707/RZ/ChipDesign/SWIFT/decayQ1/Y11Q1_Results.csv", False)
oProject.Save()