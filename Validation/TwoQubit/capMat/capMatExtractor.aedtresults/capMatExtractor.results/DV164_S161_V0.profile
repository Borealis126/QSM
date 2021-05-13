$begin 'Profile'
	$begin '56001'
		$begin 'ProfileGroup'
			MajorVer=2021
			MinorVer=1
			Name='Solution Process'
			StartInfo='Time:  05/13/2021 03:32:54; Host: c010; Processor: 36; OS: Linux 3.10.0-1160.15.2.el7.x86_64; Q3D 2021.1.0'
			TotalInfo='Elapsed time : 00:01:30 , ComEngine Memory : 99.9 M'
			GroupOptions=2
			TaskDataOptions(Memory=8)
			$begin 'ProfileGroup'
				MajorVer=2021
				MinorVer=1
				Name='Initialization'
				StartInfo='Time:  05/13/2021 03:32:54'
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
				StartInfo='Time:  05/13/2021 03:32:54'
				TotalInfo='Elapsed time : 00:00:01'
				GroupOptions=0
				TaskDataOptions(Memory=8)
				ProfileItem('  Mesh (phi surface)', 0, 0, 0, 0, 57048, 'I(1, 0, \'756 triangles\')', true, true)
			$end 'ProfileGroup'
			$begin 'ProfileGroup'
				MajorVer=2021
				MinorVer=1
				Name='Adaptive Meshing'
				StartInfo='Time:  05/13/2021 03:32:56'
				TotalInfo='Elapsed time : 00:01:29'
				GroupOptions=124
				TaskDataOptions()
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 1'
					StartInfo='Time:  05/13/2021 03:32:56'
					TotalInfo='Elapsed time : 00:00:01'
					GroupOptions=1587575344
					TaskDataOptions()
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c010 Using 16 core(s); 196496116 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 0, 0, 3, 0, 277980, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 0, 0, 0, 0, 277980, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 2'
					StartInfo='Time:  05/13/2021 03:32:57'
					TotalInfo='Elapsed time : 00:00:02'
					GroupOptions=124
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 57240, 'I(1, 0, \'2088 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c010 Using 16 core(s); 196496116 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 0, 0, 7, 0, 430424, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 0, 0, 1, 0, 430424, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 3'
					StartInfo='Time:  05/13/2021 03:33:00'
					TotalInfo='Elapsed time : 00:00:04'
					GroupOptions=1587575344
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 57264, 'I(1, 0, \'4512 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c010 Using 16 core(s); 196496116 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 2, 0, 20, 0, 851712, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 0, 0, 1, 0, 851712, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 4'
					StartInfo='Time:  05/13/2021 03:33:05'
					TotalInfo='Elapsed time : 00:00:04'
					GroupOptions=1587575344
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 57332, 'I(1, 0, \'9420 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c010 Using 16 core(s); 196496116 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 1, 0, 19, 0, 687640, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 1, 0, 6, 0, 687640, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 5'
					StartInfo='Time:  05/13/2021 03:33:09'
					TotalInfo='Elapsed time : 00:00:06'
					GroupOptions=124
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 70860, 'I(1, 0, \'20222 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c010 Using 16 core(s); 196496116 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 3, 0, 37, 0, 1040208, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 0, 0, 15, 0, 1040208, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 6'
					StartInfo='Time:  05/13/2021 03:33:16'
					TotalInfo='Elapsed time : 00:00:11'
					GroupOptions=124
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 1, 0, 1, 0, 111416, 'I(1, 0, \'40562 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c010 Using 16 core(s); 196496116 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 4, 0, 63, 0, 1049456, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 3, 0, 39, 0, 1105880, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 7'
					StartInfo='Time:  05/13/2021 03:33:27'
					TotalInfo='Elapsed time : 00:00:20'
					GroupOptions=1587575344
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 2, 0, 2, 0, 190176, 'I(1, 0, \'79710 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c010 Using 16 core(s); 196496116 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 8, 0, 96, 0, 1471556, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 6, 0, 92, 0, 1789580, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 8'
					StartInfo='Time:  05/13/2021 03:33:48'
					TotalInfo='Elapsed time : 00:00:37'
					GroupOptions=1587575344
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 4, 0, 4, 0, 327472, 'I(1, 0, \'149142 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c010 Using 16 core(s); 196496116 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 14, 0, 172, 0, 1812932, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 14, 0, 209, 0, 2497952, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				ProfileFootnote('I(1, 0, \'Adaptive Passes converged\')', 0)
			$end 'ProfileGroup'
			ProfileFootnote('I(1, 0, \'Time:  05/13/2021 03:34:25, Status: Normal Completion\')', 0)
		$end 'ProfileGroup'
	$end '56001'
$end 'Profile'
