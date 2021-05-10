$begin 'Profile'
	$begin '56001'
		$begin 'ProfileGroup'
			MajorVer=2021
			MinorVer=1
			Name='Solution Process'
			StartInfo='Time:  05/10/2021 13:56:12; Host: c049; Processor: 36; OS: Linux 3.10.0-1160.15.2.el7.x86_64; Q3D 2021.1.0'
			TotalInfo='Elapsed time : 00:01:32 , ComEngine Memory : 99.4 M'
			GroupOptions=2
			TaskDataOptions(Memory=8)
			$begin 'ProfileGroup'
				MajorVer=2021
				MinorVer=1
				Name='Initialization'
				StartInfo='Time:  05/10/2021 13:56:12'
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
				StartInfo='Time:  05/10/2021 13:56:12'
				TotalInfo='Elapsed time : 00:00:02'
				GroupOptions=0
				TaskDataOptions(Memory=8)
				ProfileItem('  Mesh (phi surface)', 1, 0, 0, 0, 57144, 'I(1, 0, \'756 triangles\')', true, true)
			$end 'ProfileGroup'
			$begin 'ProfileGroup'
				MajorVer=2021
				MinorVer=1
				Name='Adaptive Meshing'
				StartInfo='Time:  05/10/2021 13:56:15'
				TotalInfo='Elapsed time : 00:01:29'
				GroupOptions=124
				TaskDataOptions()
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 1'
					StartInfo='Time:  05/10/2021 13:56:15'
					TotalInfo='Elapsed time : 00:00:02'
					GroupOptions=1954544176
					TaskDataOptions()
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c049 Using 16 core(s); 394664584 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 0, 0, 4, 0, 277336, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 0, 0, 0, 0, 277336, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 2'
					StartInfo='Time:  05/10/2021 13:56:17'
					TotalInfo='Elapsed time : 00:00:02'
					GroupOptions=1954544176
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 57336, 'I(1, 0, \'2088 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c049 Using 16 core(s); 394664584 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 0, 0, 7, 0, 474288, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 0, 0, 1, 0, 474288, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 3'
					StartInfo='Time:  05/10/2021 13:56:20'
					TotalInfo='Elapsed time : 00:00:05'
					GroupOptions=1954544176
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 57360, 'I(1, 0, \'4512 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c049 Using 16 core(s); 394664584 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 3, 0, 20, 0, 843300, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 0, 0, 2, 0, 843300, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 4'
					StartInfo='Time:  05/10/2021 13:56:25'
					TotalInfo='Elapsed time : 00:00:04'
					GroupOptions=1954544176
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 57428, 'I(1, 0, \'9420 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c049 Using 16 core(s); 394664584 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 1, 0, 19, 0, 711264, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 1, 0, 5, 0, 711264, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 5'
					StartInfo='Time:  05/10/2021 13:56:29'
					TotalInfo='Elapsed time : 00:00:06'
					GroupOptions=1954544176
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 70856, 'I(1, 0, \'20222 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c049 Using 16 core(s); 394664584 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 2, 0, 38, 0, 1027348, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 1, 0, 14, 0, 1027348, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 6'
					StartInfo='Time:  05/10/2021 13:56:36'
					TotalInfo='Elapsed time : 00:00:10'
					GroupOptions=124
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 1, 0, 1, 0, 111428, 'I(1, 0, \'40562 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c049 Using 16 core(s); 394664584 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 4, 0, 63, 0, 1093104, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 3, 0, 38, 0, 1148684, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 7'
					StartInfo='Time:  05/10/2021 13:56:47'
					TotalInfo='Elapsed time : 00:00:18'
					GroupOptions=124
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 2, 0, 2, 0, 190176, 'I(1, 0, \'79710 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c049 Using 16 core(s); 394664584 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 7, 0, 93, 0, 1505756, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 6, 0, 88, 0, 1808104, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 8'
					StartInfo='Time:  05/10/2021 13:57:06'
					TotalInfo='Elapsed time : 00:00:37'
					GroupOptions=1954544176
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 4, 0, 4, 0, 327480, 'I(1, 0, \'149142 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c049 Using 16 core(s); 394664584 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 14, 0, 166, 0, 1799528, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 15, 0, 225, 0, 2484404, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				ProfileFootnote('I(1, 0, \'Adaptive Passes converged\')', 0)
			$end 'ProfileGroup'
			ProfileFootnote('I(1, 0, \'Time:  05/10/2021 13:57:44, Status: Normal Completion\')', 0)
		$end 'ProfileGroup'
	$end '56001'
$end 'Profile'
