import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("capMatExtractor")
oProject.InsertDesign("Q3D Extractor", "capMatExtractor", "", "")
oDesign = oProject.SetActiveDesign("capMatExtractor")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oModuleBoundary = oDesign.GetModule("BoundarySetup")
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-4750.0um",
                "Y:="			, "-3750.0um",
                "Z:="			, "0um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-4750.0um",
                "Y:="			, "3750.0um",
                "Z:="			, "0um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "4750.0um",
                "Y:="			, "3750.0um",
                "Z:="			, "0um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "4750.0um",
                "Y:="			, "-3750.0um",
                "Z:="			, "0um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-4750.0um",
                "Y:="			, "-3750.0um",
                "Z:="			, "0um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "S0",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "S0",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "500um",
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-4750.0um",
                "Y:="			, "-3750.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-4750.0um",
                "Y:="			, "3750.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "4750.0um",
                "Y:="			, "3750.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "4750.0um",
                "Y:="			, "-3750.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-4750.0um",
                "Y:="			, "-3750.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "G0",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-581.0um",
                "Y:="			, "-439.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-581.0um",
                "Y:="			, "-299.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-81.0um",
                "Y:="			, "-299.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-81.0um",
                "Y:="			, "-439.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-329.0um",
                "Y:="			, "-439.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-329.0um",
                "Y:="			, "-450.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-333.0um",
                "Y:="			, "-450.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-333.0um",
                "Y:="			, "-439.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-581.0um",
                "Y:="			, "-439.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 4,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 5,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 6,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 7,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q0Pad1",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oModuleBoundary.AssignThinConductor(
    [
        "NAME:ThinCondQ0Pad1",
        "Objects:="		, ["Q0Pad1"],
        "Material:="		, "perfect conductor",
        "Thickness:="		, "0.1um"
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-581.0um",
                "Y:="			, "-439.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-581.0um",
                "Y:="			, "-299.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-81.0um",
                "Y:="			, "-299.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-81.0um",
                "Y:="			, "-439.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-329.0um",
                "Y:="			, "-439.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-329.0um",
                "Y:="			, "-450.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-333.0um",
                "Y:="			, "-450.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-333.0um",
                "Y:="			, "-439.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-581.0um",
                "Y:="			, "-439.0um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 4,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 5,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 6,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 7,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q0Pad1TrenchComponent",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-681.0um",
                "Y:="			, "-539.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-681.0um",
                "Y:="			, "-199.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "19.0um",
                "Y:="			, "-199.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "19.0um",
                "Y:="			, "-539.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-681.0um",
                "Y:="			, "-539.0um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q0Pad1TrenchPeriphery0",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-363.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-363.0um",
                "Y:="			, "-439.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-299.0um",
                "Y:="			, "-439.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-299.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-363.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q0Pad1TrenchPeriphery1",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q0Pad1TrenchPeriphery0",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "Q0Pad1TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q0Pad1TrenchPeriphery1",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "Q0Pad1TrenchPeriphery1"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:Q0Pad1",
        "Objects:="		, ["Q0Pad1"]
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-681.0um",
                "Y:="			, "-539.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-681.0um",
                "Y:="			, "-199.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "19.0um",
                "Y:="			, "-199.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "19.0um",
                "Y:="			, "-539.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-681.0um",
                "Y:="			, "-539.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q0Pad1periphery0",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "Q0Pad1periphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-363.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-363.0um",
                "Y:="			, "-439.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-299.0um",
                "Y:="			, "-439.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-299.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-363.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q0Pad1periphery1",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "Q0Pad1periphery1"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-81.0um",
                "Y:="			, "-469.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-81.0um",
                "Y:="			, "-609.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-581.0um",
                "Y:="			, "-609.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-581.0um",
                "Y:="			, "-469.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-333.0um",
                "Y:="			, "-469.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-333.0um",
                "Y:="			, "-458.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-329.0um",
                "Y:="			, "-458.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-329.0um",
                "Y:="			, "-469.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-81.0um",
                "Y:="			, "-469.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 4,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 5,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 6,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 7,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q0Pad2",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oModuleBoundary.AssignThinConductor(
    [
        "NAME:ThinCondQ0Pad2",
        "Objects:="		, ["Q0Pad2"],
        "Material:="		, "perfect conductor",
        "Thickness:="		, "0.1um"
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-81.0um",
                "Y:="			, "-469.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-81.0um",
                "Y:="			, "-609.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-581.0um",
                "Y:="			, "-609.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-581.0um",
                "Y:="			, "-469.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-333.0um",
                "Y:="			, "-469.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-333.0um",
                "Y:="			, "-458.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-329.0um",
                "Y:="			, "-458.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-329.0um",
                "Y:="			, "-469.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-81.0um",
                "Y:="			, "-469.0um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 4,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 5,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 6,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 7,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q0Pad2TrenchComponent",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "19.0um",
                "Y:="			, "-369.00000000000006um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "19.0um",
                "Y:="			, "-709.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-681.0um",
                "Y:="			, "-709.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-681.0um",
                "Y:="			, "-368.99999999999994um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "19.0um",
                "Y:="			, "-369.00000000000006um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q0Pad2TrenchPeriphery0",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-299.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-299.0um",
                "Y:="			, "-469.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-363.0um",
                "Y:="			, "-469.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-363.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-299.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q0Pad2TrenchPeriphery1",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q0Pad2TrenchPeriphery0",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "Q0Pad2TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q0Pad2TrenchPeriphery1",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "Q0Pad2TrenchPeriphery1"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:Q0Pad2",
        "Objects:="		, ["Q0Pad2"]
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "19.0um",
                "Y:="			, "-369.00000000000006um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "19.0um",
                "Y:="			, "-709.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-681.0um",
                "Y:="			, "-709.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-681.0um",
                "Y:="			, "-368.99999999999994um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "19.0um",
                "Y:="			, "-369.00000000000006um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q0Pad2periphery0",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "Q0Pad2periphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-299.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-299.0um",
                "Y:="			, "-469.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-363.0um",
                "Y:="			, "-469.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-363.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-299.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q0Pad2periphery1",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "Q0Pad2periphery1"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "81.0um",
                "Y:="			, "-421.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "81.0um",
                "Y:="			, "-301.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "581.0um",
                "Y:="			, "-301.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "581.0um",
                "Y:="			, "-421.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "333.0um",
                "Y:="			, "-421.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "333.0um",
                "Y:="			, "-450.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "329.0um",
                "Y:="			, "-450.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "329.0um",
                "Y:="			, "-421.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "81.0um",
                "Y:="			, "-421.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 4,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 5,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 6,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 7,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q1Pad1",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oModuleBoundary.AssignThinConductor(
    [
        "NAME:ThinCondQ1Pad1",
        "Objects:="		, ["Q1Pad1"],
        "Material:="		, "perfect conductor",
        "Thickness:="		, "0.1um"
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "81.0um",
                "Y:="			, "-421.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "81.0um",
                "Y:="			, "-301.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "581.0um",
                "Y:="			, "-301.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "581.0um",
                "Y:="			, "-421.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "333.0um",
                "Y:="			, "-421.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "333.0um",
                "Y:="			, "-450.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "329.0um",
                "Y:="			, "-450.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "329.0um",
                "Y:="			, "-421.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "81.0um",
                "Y:="			, "-421.0um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 4,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 5,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 6,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 7,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q1Pad1TrenchComponent",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-19.0um",
                "Y:="			, "-521.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-19.0um",
                "Y:="			, "-199.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "681.0um",
                "Y:="			, "-199.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "681.0um",
                "Y:="			, "-521.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-19.0um",
                "Y:="			, "-521.0um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q1Pad1TrenchPeriphery0",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "299.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "299.0um",
                "Y:="			, "-421.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "363.0um",
                "Y:="			, "-421.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "363.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "299.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q1Pad1TrenchPeriphery1",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q1Pad1TrenchPeriphery0",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "Q1Pad1TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q1Pad1TrenchPeriphery1",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "Q1Pad1TrenchPeriphery1"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:Q1Pad1",
        "Objects:="		, ["Q1Pad1"]
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-19.0um",
                "Y:="			, "-521.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-19.0um",
                "Y:="			, "-199.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "681.0um",
                "Y:="			, "-199.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "681.0um",
                "Y:="			, "-521.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-19.0um",
                "Y:="			, "-521.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q1Pad1periphery0",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "Q1Pad1periphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "299.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "299.0um",
                "Y:="			, "-421.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "363.0um",
                "Y:="			, "-421.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "363.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "299.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q1Pad1periphery1",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "Q1Pad1periphery1"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "581.0um",
                "Y:="			, "-487.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "581.0um",
                "Y:="			, "-607.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "81.0um",
                "Y:="			, "-607.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "81.0um",
                "Y:="			, "-487.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "329.0um",
                "Y:="			, "-487.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "329.0um",
                "Y:="			, "-458.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "333.0um",
                "Y:="			, "-458.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "333.0um",
                "Y:="			, "-487.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "581.0um",
                "Y:="			, "-487.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 4,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 5,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 6,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 7,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q1Pad2",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oModuleBoundary.AssignThinConductor(
    [
        "NAME:ThinCondQ1Pad2",
        "Objects:="		, ["Q1Pad2"],
        "Material:="		, "perfect conductor",
        "Thickness:="		, "0.1um"
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "581.0um",
                "Y:="			, "-487.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "581.0um",
                "Y:="			, "-607.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "81.0um",
                "Y:="			, "-607.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "81.0um",
                "Y:="			, "-487.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "329.0um",
                "Y:="			, "-487.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "329.0um",
                "Y:="			, "-458.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "333.0um",
                "Y:="			, "-458.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "333.0um",
                "Y:="			, "-487.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "581.0um",
                "Y:="			, "-487.0um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 4,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 5,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 6,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 7,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q1Pad2TrenchComponent",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "681.0um",
                "Y:="			, "-387.00000000000006um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "681.0um",
                "Y:="			, "-709.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-19.0um",
                "Y:="			, "-709.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-19.0um",
                "Y:="			, "-386.99999999999994um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "681.0um",
                "Y:="			, "-387.00000000000006um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q1Pad2TrenchPeriphery0",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "363.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "363.0um",
                "Y:="			, "-487.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "299.0um",
                "Y:="			, "-487.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "299.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "363.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q1Pad2TrenchPeriphery1",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q1Pad2TrenchPeriphery0",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "Q1Pad2TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q1Pad2TrenchPeriphery1",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "Q1Pad2TrenchPeriphery1"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:Q1Pad2",
        "Objects:="		, ["Q1Pad2"]
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "681.0um",
                "Y:="			, "-387.00000000000006um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "681.0um",
                "Y:="			, "-709.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-19.0um",
                "Y:="			, "-709.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-19.0um",
                "Y:="			, "-386.99999999999994um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "681.0um",
                "Y:="			, "-387.00000000000006um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q1Pad2periphery0",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "Q1Pad2periphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "363.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "363.0um",
                "Y:="			, "-487.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "299.0um",
                "Y:="			, "-487.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "299.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "363.0um",
                "Y:="			, "-454.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "Q1Pad2periphery1",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "Q1Pad2periphery1"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-895.54um",
                "Y:="			, "2406.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-895.54um",
                "Y:="			, "2396.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1090.54um",
                "Y:="			, "2396.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1090.54um",
                "Y:="			, "2371.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1090.54um",
                "Y:="			, "2371.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1090.54um",
                "Y:="			, "2346.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1100.54um",
                "Y:="			, "2346.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1100.54um",
                "Y:="			, "2371.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1100.54um",
                "Y:="			, "2371.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1100.54um",
                "Y:="			, "2396.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1295.54um",
                "Y:="			, "2396.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1295.54um",
                "Y:="			, "2406.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-895.54um",
                "Y:="			, "2406.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 4,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 5,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 6,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 7,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 8,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 9,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 10,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 11,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R0Pad1",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oModuleBoundary.AssignThinConductor(
    [
        "NAME:ThinCondR0Pad1",
        "Objects:="		, ["R0Pad1"],
        "Material:="		, "perfect conductor",
        "Thickness:="		, "0.1um"
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-895.54um",
                "Y:="			, "2406.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-895.54um",
                "Y:="			, "2396.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1090.54um",
                "Y:="			, "2396.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1090.54um",
                "Y:="			, "2371.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1090.54um",
                "Y:="			, "2371.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1090.54um",
                "Y:="			, "2346.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1100.54um",
                "Y:="			, "2346.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1100.54um",
                "Y:="			, "2371.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1100.54um",
                "Y:="			, "2371.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1100.54um",
                "Y:="			, "2396.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1295.54um",
                "Y:="			, "2396.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1295.54um",
                "Y:="			, "2406.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-895.54um",
                "Y:="			, "2406.0um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 4,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 5,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 6,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 7,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 8,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 9,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 10,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 11,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R0Pad1TrenchComponent",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-871.54um",
                "Y:="			, "2412.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-871.54um",
                "Y:="			, "2390.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1319.54um",
                "Y:="			, "2390.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1319.54um",
                "Y:="			, "2412.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-871.54um",
                "Y:="			, "2412.0um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R0Pad1TrenchPeriphery0",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-1084.54um",
                "Y:="			, "2402.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1084.54um",
                "Y:="			, "2365.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1106.54um",
                "Y:="			, "2365.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1106.54um",
                "Y:="			, "2402.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1084.54um",
                "Y:="			, "2402.0um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R0Pad1TrenchPeriphery1",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-1084.54um",
                "Y:="			, "2372.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1084.54um",
                "Y:="			, "2345.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1106.54um",
                "Y:="			, "2345.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1106.54um",
                "Y:="			, "2372.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1084.54um",
                "Y:="			, "2372.0um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R0Pad1TrenchPeriphery2",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R0Pad1TrenchPeriphery0",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "R0Pad1TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R0Pad1TrenchPeriphery1",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "R0Pad1TrenchPeriphery1"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R0Pad1TrenchPeriphery2",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "R0Pad1TrenchPeriphery2"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:R0Pad1",
        "Objects:="		, ["R0Pad1"]
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-871.54um",
                "Y:="			, "2412.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-871.54um",
                "Y:="			, "2390.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1319.54um",
                "Y:="			, "2390.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1319.54um",
                "Y:="			, "2412.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-871.54um",
                "Y:="			, "2412.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R0Pad1periphery0",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "R0Pad1periphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-1084.54um",
                "Y:="			, "2402.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1084.54um",
                "Y:="			, "2365.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1106.54um",
                "Y:="			, "2365.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1106.54um",
                "Y:="			, "2402.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1084.54um",
                "Y:="			, "2402.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R0Pad1periphery1",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "R0Pad1periphery1"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-1084.54um",
                "Y:="			, "2372.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1084.54um",
                "Y:="			, "2345.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1106.54um",
                "Y:="			, "2345.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1106.54um",
                "Y:="			, "2372.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-1084.54um",
                "Y:="			, "2372.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R0Pad1periphery2",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "R0Pad1periphery2"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-589.0047524716616um",
                "Y:="			, "-400.5352474141841um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-619.0047524716616um",
                "Y:="			, "-400.53524742033716um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-619.0047524808912um",
                "Y:="			, "-355.53524742033716um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-644.0047524808912um",
                "Y:="			, "-355.5352474254648um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-644.0047524808912um",
                "Y:="			, "-355.5352474254648um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-669.0047524808913um",
                "Y:="			, "-355.53524743059234um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-669.0047524829422um",
                "Y:="			, "-345.53524743059234um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-644.0047524829423um",
                "Y:="			, "-345.5352474254648um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-644.0047524829423um",
                "Y:="			, "-345.5352474254648um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-619.0047524829423um",
                "Y:="			, "-345.53524742033716um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-619.0047524921719um",
                "Y:="			, "-300.53524742033716um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-589.0047524921719um",
                "Y:="			, "-300.5352474141841um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-589.0047524716616um",
                "Y:="			, "-400.5352474141841um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 4,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 5,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 6,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 7,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 8,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 9,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 10,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 11,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R0Pad2",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oModuleBoundary.AssignThinConductor(
    [
        "NAME:ThinCondR0Pad2",
        "Objects:="		, ["R0Pad2"],
        "Material:="		, "perfect conductor",
        "Thickness:="		, "0.1um"
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-589.0047524716616um",
                "Y:="			, "-400.5352474141841um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-619.0047524716616um",
                "Y:="			, "-400.53524742033716um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-619.0047524808912um",
                "Y:="			, "-355.53524742033716um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-644.0047524808912um",
                "Y:="			, "-355.5352474254648um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-644.0047524808912um",
                "Y:="			, "-355.5352474254648um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-669.0047524808913um",
                "Y:="			, "-355.53524743059234um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-669.0047524829422um",
                "Y:="			, "-345.53524743059234um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-644.0047524829423um",
                "Y:="			, "-345.5352474254648um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-644.0047524829423um",
                "Y:="			, "-345.5352474254648um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-619.0047524829423um",
                "Y:="			, "-345.53524742033716um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-619.0047524921719um",
                "Y:="			, "-300.53524742033716um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-589.0047524921719um",
                "Y:="			, "-300.5352474141841um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-589.0047524716616um",
                "Y:="			, "-400.5352474141841um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 4,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 5,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 6,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 7,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 8,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 9,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 10,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 11,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R0Pad2TrenchComponent",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-559.0047524655084um",
                "Y:="			, "-430.53524740803095um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-649.0047524655084um",
                "Y:="			, "-430.5352474264903um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-649.004752498325um",
                "Y:="			, "-270.5352474264903um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-559.004752498325um",
                "Y:="			, "-270.53524740803095um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-559.0047524655084um",
                "Y:="			, "-430.53524740803095um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R0Pad2TrenchPeriphery0",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-613.0047524796606um",
                "Y:="			, "-361.53524741910655um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-650.0047524796606um",
                "Y:="			, "-361.5352474266954um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-650.0047524841729um",
                "Y:="			, "-339.5352474266954um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-613.0047524841729um",
                "Y:="			, "-339.53524741910655um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-613.0047524796606um",
                "Y:="			, "-361.53524741910655um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R0Pad2TrenchPeriphery1",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-643.0047524796606um",
                "Y:="			, "-361.5352474252596um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-670.0047524796606um",
                "Y:="			, "-361.5352474307974um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-670.0047524841729um",
                "Y:="			, "-339.5352474307974um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-643.0047524841729um",
                "Y:="			, "-339.5352474252596um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-643.0047524796606um",
                "Y:="			, "-361.5352474252596um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R0Pad2TrenchPeriphery2",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R0Pad2TrenchPeriphery0",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "R0Pad2TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R0Pad2TrenchPeriphery1",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "R0Pad2TrenchPeriphery1"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R0Pad2TrenchPeriphery2",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "R0Pad2TrenchPeriphery2"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:R0Pad2",
        "Objects:="		, ["R0Pad2"]
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-559.0047524655084um",
                "Y:="			, "-430.53524740803095um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-649.0047524655084um",
                "Y:="			, "-430.5352474264903um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-649.004752498325um",
                "Y:="			, "-270.5352474264903um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-559.004752498325um",
                "Y:="			, "-270.53524740803095um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-559.0047524655084um",
                "Y:="			, "-430.53524740803095um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R0Pad2periphery0",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "R0Pad2periphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-613.0047524796606um",
                "Y:="			, "-361.53524741910655um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-650.0047524796606um",
                "Y:="			, "-361.5352474266954um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-650.0047524841729um",
                "Y:="			, "-339.5352474266954um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-613.0047524841729um",
                "Y:="			, "-339.53524741910655um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-613.0047524796606um",
                "Y:="			, "-361.53524741910655um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R0Pad2periphery1",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "R0Pad2periphery1"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-643.0047524796606um",
                "Y:="			, "-361.5352474252596um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-670.0047524796606um",
                "Y:="			, "-361.5352474307974um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-670.0047524841729um",
                "Y:="			, "-339.5352474307974um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-643.0047524841729um",
                "Y:="			, "-339.5352474252596um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-643.0047524796606um",
                "Y:="			, "-361.5352474252596um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R0Pad2periphery2",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "R0Pad2periphery2"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "1316.0um",
                "Y:="			, "2406.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1316.0um",
                "Y:="			, "2396.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1121.0um",
                "Y:="			, "2396.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1121.0um",
                "Y:="			, "2371.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1121.0um",
                "Y:="			, "2371.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1121.0um",
                "Y:="			, "2346.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1111.0um",
                "Y:="			, "2346.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1111.0um",
                "Y:="			, "2371.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1111.0um",
                "Y:="			, "2371.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1111.0um",
                "Y:="			, "2396.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "916.0um",
                "Y:="			, "2396.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "916.0um",
                "Y:="			, "2406.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1316.0um",
                "Y:="			, "2406.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 4,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 5,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 6,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 7,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 8,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 9,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 10,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 11,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R1Pad1",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oModuleBoundary.AssignThinConductor(
    [
        "NAME:ThinCondR1Pad1",
        "Objects:="		, ["R1Pad1"],
        "Material:="		, "perfect conductor",
        "Thickness:="		, "0.1um"
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "1316.0um",
                "Y:="			, "2406.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1316.0um",
                "Y:="			, "2396.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1121.0um",
                "Y:="			, "2396.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1121.0um",
                "Y:="			, "2371.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1121.0um",
                "Y:="			, "2371.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1121.0um",
                "Y:="			, "2346.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1111.0um",
                "Y:="			, "2346.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1111.0um",
                "Y:="			, "2371.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1111.0um",
                "Y:="			, "2371.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1111.0um",
                "Y:="			, "2396.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "916.0um",
                "Y:="			, "2396.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "916.0um",
                "Y:="			, "2406.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1316.0um",
                "Y:="			, "2406.0um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 4,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 5,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 6,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 7,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 8,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 9,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 10,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 11,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R1Pad1TrenchComponent",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "1340.0um",
                "Y:="			, "2412.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1340.0um",
                "Y:="			, "2390.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "892.0um",
                "Y:="			, "2390.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "892.0um",
                "Y:="			, "2412.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1340.0um",
                "Y:="			, "2412.0um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R1Pad1TrenchPeriphery0",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "1127.0um",
                "Y:="			, "2402.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1127.0um",
                "Y:="			, "2365.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1105.0um",
                "Y:="			, "2365.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1105.0um",
                "Y:="			, "2402.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1127.0um",
                "Y:="			, "2402.0um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R1Pad1TrenchPeriphery1",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "1127.0um",
                "Y:="			, "2372.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1127.0um",
                "Y:="			, "2345.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1105.0um",
                "Y:="			, "2345.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1105.0um",
                "Y:="			, "2372.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1127.0um",
                "Y:="			, "2372.0um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R1Pad1TrenchPeriphery2",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R1Pad1TrenchPeriphery0",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "R1Pad1TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R1Pad1TrenchPeriphery1",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "R1Pad1TrenchPeriphery1"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R1Pad1TrenchPeriphery2",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "R1Pad1TrenchPeriphery2"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:R1Pad1",
        "Objects:="		, ["R1Pad1"]
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "1340.0um",
                "Y:="			, "2412.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1340.0um",
                "Y:="			, "2390.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "892.0um",
                "Y:="			, "2390.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "892.0um",
                "Y:="			, "2412.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1340.0um",
                "Y:="			, "2412.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R1Pad1periphery0",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "R1Pad1periphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "1127.0um",
                "Y:="			, "2402.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1127.0um",
                "Y:="			, "2365.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1105.0um",
                "Y:="			, "2365.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1105.0um",
                "Y:="			, "2402.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1127.0um",
                "Y:="			, "2402.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R1Pad1periphery1",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "R1Pad1periphery1"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "1127.0um",
                "Y:="			, "2372.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1127.0um",
                "Y:="			, "2345.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1105.0um",
                "Y:="			, "2345.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1105.0um",
                "Y:="			, "2372.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "1127.0um",
                "Y:="			, "2372.0um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R1Pad1periphery2",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "R1Pad1periphery2"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "609.1464426059927um",
                "Y:="			, "-301.3535573003295um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "639.1464426059927um",
                "Y:="			, "-301.35355730648257um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "639.146442596763um",
                "Y:="			, "-346.35355730648257um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "664.146442596763um",
                "Y:="			, "-346.3535573116102um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "664.146442596763um",
                "Y:="			, "-346.3535573116102um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "689.1464425967629um",
                "Y:="			, "-346.35355731673775um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "689.146442594712um",
                "Y:="			, "-356.35355731673775um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "664.1464425947119um",
                "Y:="			, "-356.3535573116102um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "664.1464425947119um",
                "Y:="			, "-356.3535573116102um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "639.1464425947119um",
                "Y:="			, "-356.35355730648257um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "639.1464425854822um",
                "Y:="			, "-401.35355730648257um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "609.1464425854822um",
                "Y:="			, "-401.3535573003295um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "609.1464426059927um",
                "Y:="			, "-301.3535573003295um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 4,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 5,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 6,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 7,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 8,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 9,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 10,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 11,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R1Pad2",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oModuleBoundary.AssignThinConductor(
    [
        "NAME:ThinCondR1Pad2",
        "Objects:="		, ["R1Pad2"],
        "Material:="		, "perfect conductor",
        "Thickness:="		, "0.1um"
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "609.1464426059927um",
                "Y:="			, "-301.3535573003295um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "639.1464426059927um",
                "Y:="			, "-301.35355730648257um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "639.146442596763um",
                "Y:="			, "-346.35355730648257um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "664.146442596763um",
                "Y:="			, "-346.3535573116102um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "664.146442596763um",
                "Y:="			, "-346.3535573116102um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "689.1464425967629um",
                "Y:="			, "-346.35355731673775um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "689.146442594712um",
                "Y:="			, "-356.35355731673775um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "664.1464425947119um",
                "Y:="			, "-356.3535573116102um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "664.1464425947119um",
                "Y:="			, "-356.3535573116102um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "639.1464425947119um",
                "Y:="			, "-356.35355730648257um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "639.1464425854822um",
                "Y:="			, "-401.35355730648257um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "609.1464425854822um",
                "Y:="			, "-401.3535573003295um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "609.1464426059927um",
                "Y:="			, "-301.3535573003295um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 4,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 5,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 6,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 7,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 8,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 9,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 10,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 11,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R1Pad2TrenchComponent",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "579.1464426121457um",
                "Y:="			, "-271.35355729417637um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "669.1464426121457um",
                "Y:="			, "-271.3535573126357um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "669.1464425793291um",
                "Y:="			, "-431.3535573126357um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "579.1464425793291um",
                "Y:="			, "-431.35355729417637um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "579.1464426121457um",
                "Y:="			, "-271.35355729417637um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R1Pad2TrenchPeriphery0",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "633.1464425979935um",
                "Y:="			, "-340.35355730525197um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "670.1464425979935um",
                "Y:="			, "-340.3535573128408um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "670.1464425934813um",
                "Y:="			, "-362.3535573128408um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "633.1464425934813um",
                "Y:="			, "-362.35355730525197um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "633.1464425979935um",
                "Y:="			, "-340.35355730525197um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R1Pad2TrenchPeriphery1",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "663.1464425979935um",
                "Y:="			, "-340.3535573114051um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "690.1464425979935um",
                "Y:="			, "-340.3535573169429um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "690.1464425934813um",
                "Y:="			, "-362.3535573169429um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "663.1464425934813um",
                "Y:="			, "-362.3535573114051um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "663.1464425979935um",
                "Y:="			, "-340.3535573114051um",
                "Z:="			, "499.9um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R1Pad2TrenchPeriphery2",
        "Flags:="		, "",
        "Color:="		, "(143 175 143)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"silicon\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, True,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R1Pad2TrenchPeriphery0",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "R1Pad2TrenchPeriphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R1Pad2TrenchPeriphery1",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "R1Pad2TrenchPeriphery1"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R1Pad2TrenchPeriphery2",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "S0",
        "Tool Parts:="		, "R1Pad2TrenchPeriphery2"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:R1Pad2",
        "Objects:="		, ["R1Pad2"]
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "579.1464426121457um",
                "Y:="			, "-271.35355729417637um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "669.1464426121457um",
                "Y:="			, "-271.3535573126357um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "669.1464425793291um",
                "Y:="			, "-431.3535573126357um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "579.1464425793291um",
                "Y:="			, "-431.35355729417637um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "579.1464426121457um",
                "Y:="			, "-271.35355729417637um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R1Pad2periphery0",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "R1Pad2periphery0"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "633.1464425979935um",
                "Y:="			, "-340.35355730525197um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "670.1464425979935um",
                "Y:="			, "-340.3535573128408um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "670.1464425934813um",
                "Y:="			, "-362.3535573128408um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "633.1464425934813um",
                "Y:="			, "-362.35355730525197um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "633.1464425979935um",
                "Y:="			, "-340.35355730525197um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R1Pad2periphery1",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "R1Pad2periphery1"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "663.1464425979935um",
                "Y:="			, "-340.3535573114051um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "690.1464425979935um",
                "Y:="			, "-340.3535573169429um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "690.1464425934813um",
                "Y:="			, "-362.3535573169429um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "663.1464425934813um",
                "Y:="			, "-362.3535573114051um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "663.1464425979935um",
                "Y:="			, "-340.3535573114051um",
                "Z:="			, "500um"
            ]
        ],
        [
            "NAME:PolylineSegments",
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 0,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 1,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 2,
                "NoOfPoints:="		, 2
            ],
            [
                "NAME:PLSegment",
                "SegmentType:="		, "Line",
                "StartIndex:="		, 3,
                "NoOfPoints:="		, 2
            ]
        ],
        [
            "NAME:PolylineXSection",
            "XSectionType:="	, "None",
            "XSectionOrient:="	, "Auto",
            "XSectionWidth:="	, "0mm",
            "XSectionTopWidth:="	, "0mm",
            "XSectionHeight:="	, "0mm",
            "XSectionNumSegments:="	, "0",
            "XSectionBendType:="	, "Corner"
        ]
    ],
    [
        "NAME:Attributes",
        "Name:="		, "R1Pad2periphery2",
        "Flags:="		, "",
        "Color:="		, "(143 143 175)",
        "Transparency:="	, 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:="		, "",
        "MaterialValue:="	, "\"perfect conductor\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:="		, False,
        "IsMaterialEditable:="	, True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:="	, False
    ])
oEditor.Subtract(
    [
        "NAME:Selections",
        "Blank Parts:="		, "G0",
        "Tool Parts:="		, "R1Pad2periphery2"
    ],
    [
        "NAME:SubtractParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q0Pad1TrenchComponent",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Unite(
    [
        "NAME:Selections",
        "Selections:="		, "S0,Q0Pad1TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q0Pad2TrenchComponent",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Unite(
    [
        "NAME:Selections",
        "Selections:="		, "S0,Q0Pad2TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q1Pad1TrenchComponent",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Unite(
    [
        "NAME:Selections",
        "Selections:="		, "S0,Q1Pad1TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "Q1Pad2TrenchComponent",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Unite(
    [
        "NAME:Selections",
        "Selections:="		, "S0,Q1Pad2TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R0Pad1TrenchComponent",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Unite(
    [
        "NAME:Selections",
        "Selections:="		, "S0,R0Pad1TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R0Pad2TrenchComponent",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Unite(
    [
        "NAME:Selections",
        "Selections:="		, "S0,R0Pad2TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R1Pad1TrenchComponent",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Unite(
    [
        "NAME:Selections",
        "Selections:="		, "S0,R1Pad1TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oEditor.SweepAlongVector(
    [
        "NAME:Selections",
        "Selections:="		, "R1Pad2TrenchComponent",
        "NewPartsModelFlag:="	, "Model"
    ],
    [
        "NAME:VectorSweepParameters",
        "DraftAngle:="		, "0deg",
        "DraftType:="		, "Round",
        "CheckFaceFaceIntersection:=", False,
        "SweepVectorX:="	, "0mm",
        "SweepVectorY:="	, "0mm",
        "SweepVectorZ:="	, "0.1um",
    ])
oEditor.Unite(
    [
        "NAME:Selections",
        "Selections:="		, "S0,R1Pad2TrenchComponent"
    ],
    [
        "NAME:UniteParameters",
        "KeepOriginals:="	, False
    ])
oModuleBoundary.AssignThinConductor(
    [
        "NAME:ThinCondG0",
        "Objects:="		, ["G0"],
        "Material:="		, "perfect conductor",
        "Thickness:="		, "0.1um"
    ])
oModuleBoundary.AssignGroundNet(
    [
        "NAME:GroundNet1",
        "Objects:="		, ["G0"]
    ])
oModuleAnalysis = oDesign.GetModule("AnalysisSetup")
oModuleAnalysis.InsertSetup("Matrix",
    [
        "NAME:capSim",
        "AdaptiveFreq:="	, "5GHz",
        "SaveFields:="		, False,
        "Enabled:="		, True,
        [
            "NAME:Cap",
            "MaxPass:="		, 99,
            "MinPass:="		, 1,
            "MinConvPass:="		, 1,
            "PerError:="		, 1,
            "PerRefine:="		, 100,
            "AutoIncreaseSolutionOrder:=", True,
            "SolutionOrder:="	, "High",
            "Solver Type:="		, "Iterative"
        ]
    ])
oDesign.AnalyzeAll()
oDesign.ExportMatrixData("/beegfs/scratch/joelhoward/QSMSimulations/QSMSource/Example/TwoQubit/capMat/capMatExtractor_Results.csv", "C", "", "capSim:LastAdaptive", "Original", "ohm", "nH", "pF", "mSie", 5000000000, "Maxwell,Spice,Couple", 0, False, 5, 8, 0)
oProject.Save()
