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
                "Y:="			, "-201.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "681.0um",
                "Y:="			, "-201.0um",
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
                "Y:="			, "-201.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "681.0um",
                "Y:="			, "-201.0um",
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
                "Y:="			, "-707.0um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-19.0um",
                "Y:="			, "-707.0um",
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
                "Y:="			, "-707.0um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-19.0um",
                "Y:="			, "-707.0um",
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
                "X:="			, "-589.0060494772581um",
                "Y:="			, "-400.537471610032um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-619.0060494766577um",
                "Y:="			, "-400.5372818061851um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-619.0057647708874um",
                "Y:="			, "-355.5372818070857um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-644.0057647703869um",
                "Y:="			, "-355.5371236372133um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-644.0057647703869um",
                "Y:="			, "-355.5371236372133um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-669.0057647698866um",
                "Y:="			, "-355.53696546734085um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-669.0057015019377um",
                "Y:="			, "-345.536965467541um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-644.005701502438um",
                "Y:="			, "-345.53712363741346um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-644.005701502438um",
                "Y:="			, "-345.53712363741346um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-619.0057015029383um",
                "Y:="			, "-345.53728180728586um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-619.005416797168um",
                "Y:="			, "-300.5372818081865um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-589.0054167977684um",
                "Y:="			, "-300.5374716120334um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-589.0060494772581um",
                "Y:="			, "-400.537471610032um",
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
                "X:="			, "-589.0060494772581um",
                "Y:="			, "-400.537471610032um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-619.0060494766577um",
                "Y:="			, "-400.5372818061851um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-619.0057647708874um",
                "Y:="			, "-355.5372818070857um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-644.0057647703869um",
                "Y:="			, "-355.5371236372133um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-644.0057647703869um",
                "Y:="			, "-355.5371236372133um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-669.0057647698866um",
                "Y:="			, "-355.53696546734085um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-669.0057015019377um",
                "Y:="			, "-345.536965467541um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-644.005701502438um",
                "Y:="			, "-345.53712363741346um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-644.005701502438um",
                "Y:="			, "-345.53712363741346um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-619.0057015029383um",
                "Y:="			, "-345.53728180728586um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-619.005416797168um",
                "Y:="			, "-300.5372818081865um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-589.0054167977684um",
                "Y:="			, "-300.5374716120334um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-589.0060494772581um",
                "Y:="			, "-400.537471610032um",
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
                "X:="			, "-559.0062392817055um",
                "Y:="			, "-430.5376614132785um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-649.0062392799042um",
                "Y:="			, "-430.53709200173773um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-649.0052269927206um",
                "Y:="			, "-270.53709200494um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-559.0052269945219um",
                "Y:="			, "-270.5376614164808um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-559.0062392817055um",
                "Y:="			, "-430.5376614132785um",
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
                "X:="			, "-613.0058027317768um",
                "Y:="			, "-361.537319767735um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-650.0058027310363um",
                "Y:="			, "-361.53708567632384um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-650.0056635415485um",
                "Y:="			, "-339.53708567676415um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-613.0056635422891um",
                "Y:="			, "-339.53731976817534um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-613.0058027317768um",
                "Y:="			, "-361.537319767735um",
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
                "X:="			, "-643.0058027311763um",
                "Y:="			, "-361.5371299638881um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-670.005802730636um",
                "Y:="			, "-361.5369591404259um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-670.0056635411482um",
                "Y:="			, "-339.5369591408662um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-643.0056635416886um",
                "Y:="			, "-339.5371299643284um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-643.0058027311763um",
                "Y:="			, "-361.5371299638881um",
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
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "-559.0062392817055um",
                "Y:="			, "-430.5376614132785um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-649.0062392799042um",
                "Y:="			, "-430.53709200173773um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-649.0052269927206um",
                "Y:="			, "-270.53709200494um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-559.0052269945219um",
                "Y:="			, "-270.5376614164808um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-559.0062392817055um",
                "Y:="			, "-430.5376614132785um",
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
                "X:="			, "-613.0058027317768um",
                "Y:="			, "-361.537319767735um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-650.0058027310363um",
                "Y:="			, "-361.53708567632384um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-650.0056635415485um",
                "Y:="			, "-339.53708567676415um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-613.0056635422891um",
                "Y:="			, "-339.53731976817534um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-613.0058027317768um",
                "Y:="			, "-361.537319767735um",
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
                "X:="			, "-643.0058027311763um",
                "Y:="			, "-361.5371299638881um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-670.005802730636um",
                "Y:="			, "-361.5369591404259um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-670.0056635411482um",
                "Y:="			, "-339.5369591408662um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-643.0056635416886um",
                "Y:="			, "-339.5371299643284um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "-643.0058027311763um",
                "Y:="			, "-361.5371299638881um",
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
                "X:="			, "609.14710764342um",
                "Y:="			, "-301.3557827802958um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "639.1471076428195um",
                "Y:="			, "-301.35559297644886um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "639.1473923485898um",
                "Y:="			, "-346.35559297554823um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "664.1473923480895um",
                "Y:="			, "-346.3554348056758um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "664.1473923480895um",
                "Y:="			, "-346.3554348056758um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "689.1473923475892um",
                "Y:="			, "-346.3552766358034um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "689.1474556155381um",
                "Y:="			, "-356.3552766356033um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "664.1474556160384um",
                "Y:="			, "-356.3554348054757um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "664.1474556160384um",
                "Y:="			, "-356.3554348054757um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "639.1474556165389um",
                "Y:="			, "-356.3555929753481um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "639.1477403223091um",
                "Y:="			, "-401.35559297444746um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "609.1477403229096um",
                "Y:="			, "-401.3557827782944um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "609.14710764342um",
                "Y:="			, "-301.3557827802958um",
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
                "X:="			, "609.14710764342um",
                "Y:="			, "-301.3557827802958um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "639.1471076428195um",
                "Y:="			, "-301.35559297644886um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "639.1473923485898um",
                "Y:="			, "-346.35559297554823um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "664.1473923480895um",
                "Y:="			, "-346.3554348056758um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "664.1473923480895um",
                "Y:="			, "-346.3554348056758um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "689.1473923475892um",
                "Y:="			, "-346.3552766358034um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "689.1474556155381um",
                "Y:="			, "-356.3552766356033um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "664.1474556160384um",
                "Y:="			, "-356.3554348054757um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "664.1474556160384um",
                "Y:="			, "-356.3554348054757um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "639.1474556165389um",
                "Y:="			, "-356.3555929753481um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "639.1477403223091um",
                "Y:="			, "-401.35559297444746um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "609.1477403229096um",
                "Y:="			, "-401.3557827782944um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "609.14710764342um",
                "Y:="			, "-301.3557827802958um",
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
                "X:="			, "579.1469178401735um",
                "Y:="			, "-271.3559725847431um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "669.1469178383721um",
                "Y:="			, "-271.3554031732024um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "669.1479301255556um",
                "Y:="			, "-431.35540317000016um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "579.147930127357um",
                "Y:="			, "-431.35597258154087um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "579.1469178401735um",
                "Y:="			, "-271.3559725847431um",
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
                "X:="			, "633.1473543879406um",
                "Y:="			, "-340.3556309364377um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "670.1473543872um",
                "Y:="			, "-340.3553968450265um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "670.1474935766878um",
                "Y:="			, "-362.3553968445862um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "633.1474935774282um",
                "Y:="			, "-362.3556309359974um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "633.1473543879406um",
                "Y:="			, "-340.3556309364377um",
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
                "X:="			, "663.1473543873401um",
                "Y:="			, "-340.3554411325908um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "690.1473543867997um",
                "Y:="			, "-340.3552703091286um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "690.1474935762875um",
                "Y:="			, "-362.35527030868826um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "663.1474935768279um",
                "Y:="			, "-362.3554411321505um",
                "Z:="			, "499.9um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "663.1473543873401um",
                "Y:="			, "-340.3554411325908um",
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
oEditor.CreatePolyline(
    [
        "NAME:PolylineParameters",
        "IsPolylineCovered:="	, True,
        "IsPolylineClosed:="	, True,
        [
            "NAME:PolylinePoints",
            [
                "NAME:PLPoint",
                "X:="			, "579.1469178401735um",
                "Y:="			, "-271.3559725847431um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "669.1469178383721um",
                "Y:="			, "-271.3554031732024um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "669.1479301255556um",
                "Y:="			, "-431.35540317000016um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "579.147930127357um",
                "Y:="			, "-431.35597258154087um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "579.1469178401735um",
                "Y:="			, "-271.3559725847431um",
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
                "X:="			, "633.1473543879406um",
                "Y:="			, "-340.3556309364377um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "670.1473543872um",
                "Y:="			, "-340.3553968450265um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "670.1474935766878um",
                "Y:="			, "-362.3553968445862um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "633.1474935774282um",
                "Y:="			, "-362.3556309359974um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "633.1473543879406um",
                "Y:="			, "-340.3556309364377um",
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
                "X:="			, "663.1473543873401um",
                "Y:="			, "-340.3554411325908um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "690.1473543867997um",
                "Y:="			, "-340.3552703091286um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "690.1474935762875um",
                "Y:="			, "-362.35527030868826um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "663.1474935768279um",
                "Y:="			, "-362.3554411321505um",
                "Z:="			, "500um"
            ],
            [
                "NAME:PLPoint",
                "X:="			, "663.1473543873401um",
                "Y:="			, "-340.3554411325908um",
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
oModuleBoundary.AssignSignalNet(
    [
        "NAME:Q0Pad1",
        "Objects:="		, ["Q0Pad1"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:Q0Pad2",
        "Objects:="		, ["Q0Pad2"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:Q1Pad1",
        "Objects:="		, ["Q1Pad1"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:Q1Pad2",
        "Objects:="		, ["Q1Pad2"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:R0Pad1",
        "Objects:="		, ["R0Pad1"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:R0Pad2",
        "Objects:="		, ["R0Pad2"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:R1Pad1",
        "Objects:="		, ["R1Pad1"]
    ])
oModuleBoundary.AssignSignalNet(
    [
        "NAME:R1Pad2",
        "Objects:="		, ["R1Pad2"]
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
oDesign.ExportMatrixData(r"/beegfs/scratch/joelhoward/QSMSimulations/QSMSource/Validation/TwoQubit/capMat/capMatExtractor_Results.csv", "C", "", "capSim:LastAdaptive", "Original", "ohm", "nH", "pF", "mSie", 5000000000, "Maxwell,Spice,Couple", 0, False, 5, 8, 0)
oProject.Save()
