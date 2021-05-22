$begin 'Profile'
	$begin '56001'
		$begin 'ProfileGroup'
			MajorVer=2021
			MinorVer=1
			Name='Solution Process'
			StartInfo='Time:  05/21/2021 22:54:31; Host: c006; Processor: 36; OS: Linux 3.10.0-1160.15.2.el7.x86_64; Q3D 2021.1.0'
			TotalInfo='Elapsed time : 00:01:30 , ComEngine Memory : 102 M'
			GroupOptions=2
			TaskDataOptions(Memory=8)
			$begin 'ProfileGroup'
				MajorVer=2021
				MinorVer=1
				Name='Initialization'
				StartInfo='Time:  05/21/2021 22:54:31'
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
				StartInfo='Time:  05/21/2021 22:54:31'
				TotalInfo='Elapsed time : 00:00:01'
				GroupOptions=0
				TaskDataOptions(Memory=8)
				ProfileItem('  Mesh (phi surface)', 1, 0, 0, 0, 59888, 'I(1, 0, \'772 triangles\')', true, true)
			$end 'ProfileGroup'
			$begin 'ProfileGroup'
				MajorVer=2021
				MinorVer=1
				Name='Adaptive Meshing'
				StartInfo='Time:  05/21/2021 22:54:34'
				TotalInfo='Elapsed time : 00:01:28'
				GroupOptions=124
				TaskDataOptions()
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 1'
					StartInfo='Time:  05/21/2021 22:54:34'
					TotalInfo='Elapsed time : 00:00:03'
					GroupOptions=3874417200
					TaskDataOptions()
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c006 Using 16 core(s); 196496136 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 0, 0, 3, 0, 276684, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 0, 0, 1, 0, 276684, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 2'
					StartInfo='Time:  05/21/2021 22:54:37'
					TotalInfo='Elapsed time : 00:00:03'
					GroupOptions=3874417200
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 60080, 'I(1, 0, \'2142 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c006 Using 16 core(s); 196496136 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 1, 0, 7, 0, 467384, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 0, 0, 1, 0, 467384, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 3'
					StartInfo='Time:  05/21/2021 22:54:40'
					TotalInfo='Elapsed time : 00:00:03'
					GroupOptions=124
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 60104, 'I(1, 0, \'4630 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c006 Using 16 core(s); 196496136 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 1, 0, 13, 0, 614764, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 0, 0, 1, 0, 614764, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 4'
					StartInfo='Time:  05/21/2021 22:54:44'
					TotalInfo='Elapsed time : 00:00:04'
					GroupOptions=3874417200
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 60176, 'I(1, 0, \'9600 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c006 Using 16 core(s); 196496136 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 1, 0, 19, 0, 675012, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 0, 0, 5, 0, 675012, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 5'
					StartInfo='Time:  05/21/2021 22:54:48'
					TotalInfo='Elapsed time : 00:00:06'
					GroupOptions=3874417200
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 70132, 'I(1, 0, \'19852 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c006 Using 16 core(s); 196496136 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 2, 0, 34, 0, 921632, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 1, 0, 14, 0, 921632, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 6'
					StartInfo='Time:  05/21/2021 22:54:54'
					TotalInfo='Elapsed time : 00:00:10'
					GroupOptions=3874417200
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 1, 0, 1, 0, 109832, 'I(1, 0, \'39680 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c006 Using 16 core(s); 196496136 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 4, 0, 56, 0, 985044, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 2, 0, 37, 0, 1060760, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 7'
					StartInfo='Time:  05/21/2021 22:55:04'
					TotalInfo='Elapsed time : 00:00:18'
					GroupOptions=3874417200
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 2, 0, 2, 0, 183316, 'I(1, 0, \'76762 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c006 Using 16 core(s); 196496136 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 7, 0, 86, 0, 1329364, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 6, 0, 83, 0, 1624484, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 8'
					StartInfo='Time:  05/21/2021 22:55:23'
					TotalInfo='Elapsed time : 00:00:39'
					GroupOptions=3874417200
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 5, 0, 4, 0, 315976, 'I(1, 0, \'143178 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c006 Using 16 core(s); 196496136 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 19, 0, 259, 0, 3038788, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 11, 0, 157, 0, 3535776, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				ProfileFootnote('I(1, 0, \'Adaptive Passes converged\')', 0)
			$end 'ProfileGroup'
			ProfileFootnote('I(1, 0, \'Time:  05/21/2021 22:56:02, Status: Normal Completion\')', 0)
		$end 'ProfileGroup'
	$end '56001'
$end 'Profile'
