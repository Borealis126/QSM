$begin 'Profile'
	$begin '56001'
		$begin 'ProfileGroup'
			MajorVer=2021
			MinorVer=1
			Name='Solution Process'
			StartInfo='Time:  05/12/2021 12:23:21; Host: c031; Processor: 36; OS: Linux 3.10.0-1160.15.2.el7.x86_64; Q3D 2021.1.0'
			TotalInfo='Elapsed time : 00:01:31 , ComEngine Memory : 98.8 M'
			GroupOptions=2
			TaskDataOptions(Memory=8)
			$begin 'ProfileGroup'
				MajorVer=2021
				MinorVer=1
				Name='Initialization'
				StartInfo='Time:  05/12/2021 12:23:21'
				TotalInfo='Elapsed time : 00:00:00'
				GroupOptions=1
				TaskDataOptions('CPU Time'=8, Memory=8, 'Real Time'=8)
				ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 0, \'Executing from /sw/apps/ansys/ansysEM/AnsysEM21.1/Linux64/Q3DCOMENGINE.exe\')', false, true)
				ProfileItem('', 0, 0, 0, 0, 0, 'I(1, 0, \'HPC Enabled\')', false, true)
			$end 'ProfileGroup'
			$begin 'ProfileGroup'
				MajorVer=2021
				MinorVer=1
				Name='Initial Meshing'
				StartInfo='Time:  05/12/2021 12:23:21'
				TotalInfo='Elapsed time : 00:00:01'
				GroupOptions=0
				TaskDataOptions(Memory=8)
				ProfileItem('  Mesh (phi surface)', 1, 0, 0, 0, 54988, 'I(1, 0, \'756 triangles\')', true, true)
			$end 'ProfileGroup'
			$begin 'ProfileGroup'
				MajorVer=2021
				MinorVer=1
				Name='Adaptive Meshing'
				StartInfo='Time:  05/12/2021 12:23:23'
				TotalInfo='Elapsed time : 00:01:29'
				GroupOptions=124
				TaskDataOptions()
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 1'
					StartInfo='Time:  05/12/2021 12:23:23'
					TotalInfo='Elapsed time : 00:00:01'
					GroupOptions=3841968688
					TaskDataOptions()
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c031 Using 16 core(s); 196496136 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 0, 0, 3, 0, 266900, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 0, 0, 0, 0, 266900, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 2'
					StartInfo='Time:  05/12/2021 12:23:25'
					TotalInfo='Elapsed time : 00:00:03'
					GroupOptions=3841968688
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 55180, 'I(1, 0, \'2088 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c031 Using 16 core(s); 196496136 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 0, 0, 7, 0, 440352, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 0, 0, 0, 0, 440352, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 3'
					StartInfo='Time:  05/12/2021 12:23:28'
					TotalInfo='Elapsed time : 00:00:05'
					GroupOptions=124
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 55200, 'I(1, 0, \'4512 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c031 Using 16 core(s); 196496136 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 3, 0, 21, 0, 842120, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 0, 0, 1, 0, 842120, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 4'
					StartInfo='Time:  05/12/2021 12:23:33'
					TotalInfo='Elapsed time : 00:00:04'
					GroupOptions=3841968688
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 55296, 'I(1, 0, \'9420 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c031 Using 16 core(s); 196496136 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 1, 0, 19, 0, 681712, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 1, 0, 6, 0, 681712, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 5'
					StartInfo='Time:  05/12/2021 12:23:38'
					TotalInfo='Elapsed time : 00:00:07'
					GroupOptions=124
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 1, 0, 0, 0, 70860, 'I(1, 0, \'20222 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c031 Using 16 core(s); 196496136 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 3, 0, 37, 0, 1046640, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 0, 0, 15, 0, 1046640, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 6'
					StartInfo='Time:  05/12/2021 12:23:45'
					TotalInfo='Elapsed time : 00:00:11'
					GroupOptions=3841968688
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 1, 0, 1, 0, 111412, 'I(1, 0, \'40562 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c031 Using 16 core(s); 196496136 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 4, 0, 63, 0, 1080516, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 3, 0, 38, 0, 1135716, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 7'
					StartInfo='Time:  05/12/2021 12:23:56'
					TotalInfo='Elapsed time : 00:00:19'
					GroupOptions=3841968688
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 2, 0, 2, 0, 190176, 'I(1, 0, \'79710 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c031 Using 16 core(s); 196496136 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 7, 0, 93, 0, 1470948, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 6, 0, 93, 0, 1791412, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 8'
					StartInfo='Time:  05/12/2021 12:24:15'
					TotalInfo='Elapsed time : 00:00:37'
					GroupOptions=3841968688
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 4, 0, 4, 0, 327480, 'I(1, 0, \'149142 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c031 Using 16 core(s); 196496136 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 14, 0, 171, 0, 1785928, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 14, 0, 204, 0, 2469752, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				ProfileFootnote('I(1, 0, \'Adaptive Passes converged\')', 0)
			$end 'ProfileGroup'
			ProfileFootnote('I(1, 0, \'Time:  05/12/2021 12:24:52, Status: Normal Completion\')', 0)
		$end 'ProfileGroup'
	$end '56001'
$end 'Profile'
