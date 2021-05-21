$begin 'Profile'
	$begin '56001'
		$begin 'ProfileGroup'
			MajorVer=2021
			MinorVer=1
			Name='Solution Process'
			StartInfo='Time:  05/21/2021 13:46:32; Host: c018; Processor: 36; OS: Linux 3.10.0-1160.15.2.el7.x86_64; Q3D 2021.1.0'
			TotalInfo='Elapsed time : 00:01:40 , ComEngine Memory : 97.9 M'
			GroupOptions=2
			TaskDataOptions(Memory=8)
			$begin 'ProfileGroup'
				MajorVer=2021
				MinorVer=1
				Name='Initialization'
				StartInfo='Time:  05/21/2021 13:46:32'
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
				StartInfo='Time:  05/21/2021 13:46:32'
				TotalInfo='Elapsed time : 00:00:02'
				GroupOptions=0
				TaskDataOptions(Memory=8)
				ProfileItem('  Mesh (phi surface)', 1, 0, 0, 0, 55480, 'I(1, 0, \'772 triangles\')', true, true)
			$end 'ProfileGroup'
			$begin 'ProfileGroup'
				MajorVer=2021
				MinorVer=1
				Name='Adaptive Meshing'
				StartInfo='Time:  05/21/2021 13:46:35'
				TotalInfo='Elapsed time : 00:01:37'
				GroupOptions=124
				TaskDataOptions()
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 1'
					StartInfo='Time:  05/21/2021 13:46:35'
					TotalInfo='Elapsed time : 00:00:04'
					GroupOptions=4015729200
					TaskDataOptions()
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c018 Using 16 core(s); 196496136 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 1, 0, 7, 0, 290748, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 1, 0, 3, 0, 290748, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 2'
					StartInfo='Time:  05/21/2021 13:46:40'
					TotalInfo='Elapsed time : 00:00:03'
					GroupOptions=4015729200
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 55672, 'I(1, 0, \'2142 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c018 Using 16 core(s); 196496136 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 0, 0, 7, 0, 456392, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 0, 0, 1, 0, 456392, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 3'
					StartInfo='Time:  05/21/2021 13:46:43'
					TotalInfo='Elapsed time : 00:00:04'
					GroupOptions=4015729200
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 55696, 'I(1, 0, \'4630 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c018 Using 16 core(s); 196496136 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 1, 0, 13, 0, 643300, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 0, 0, 2, 0, 643300, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 4'
					StartInfo='Time:  05/21/2021 13:46:48'
					TotalInfo='Elapsed time : 00:00:06'
					GroupOptions=4015729200
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 1, 0, 0, 0, 55792, 'I(1, 0, \'9600 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c018 Using 16 core(s); 196496136 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 2, 0, 19, 0, 701012, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 0, 0, 6, 0, 701012, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 5'
					StartInfo='Time:  05/21/2021 13:46:54'
					TotalInfo='Elapsed time : 00:00:07'
					GroupOptions=4015729200
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 1, 0, 0, 0, 70396, 'I(1, 0, \'19852 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c018 Using 16 core(s); 196496136 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 2, 0, 34, 0, 945928, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 1, 0, 14, 0, 945928, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 6'
					StartInfo='Time:  05/21/2021 13:47:02'
					TotalInfo='Elapsed time : 00:00:11'
					GroupOptions=4015729200
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 1, 0, 1, 0, 109832, 'I(1, 0, \'39680 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c018 Using 16 core(s); 196496136 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 4, 0, 57, 0, 987440, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 3, 0, 34, 0, 1060628, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 7'
					StartInfo='Time:  05/21/2021 13:47:14'
					TotalInfo='Elapsed time : 00:00:19'
					GroupOptions=4015729200
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 2, 0, 2, 0, 183312, 'I(1, 0, \'76762 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c018 Using 16 core(s); 196496136 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 7, 0, 86, 0, 1362960, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 6, 0, 86, 0, 1656868, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 8'
					StartInfo='Time:  05/21/2021 13:47:33'
					TotalInfo='Elapsed time : 00:00:39'
					GroupOptions=4015729200
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 4, 0, 4, 0, 315984, 'I(1, 0, \'143178 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c018 Using 16 core(s); 196496136 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 19, 0, 259, 0, 3036540, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 11, 0, 161, 0, 3496456, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				ProfileFootnote('I(1, 0, \'Adaptive Passes converged\')', 0)
			$end 'ProfileGroup'
			ProfileFootnote('I(1, 0, \'Time:  05/21/2021 13:48:13, Status: Normal Completion\')', 0)
		$end 'ProfileGroup'
	$end '56001'
$end 'Profile'
