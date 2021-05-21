$begin 'Profile'
	$begin '56001'
		$begin 'ProfileGroup'
			MajorVer=2021
			MinorVer=1
			Name='Solution Process'
			StartInfo='Time:  05/19/2021 20:57:10; Host: c022; Processor: 36; OS: Linux 3.10.0-1160.15.2.el7.x86_64; Q3D 2021.1.0'
			TotalInfo='Elapsed time : 00:09:25 , ComEngine Memory : 103 M'
			GroupOptions=2
			TaskDataOptions(Memory=8)
			$begin 'ProfileGroup'
				MajorVer=2021
				MinorVer=1
				Name='Initialization'
				StartInfo='Time:  05/19/2021 20:57:11'
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
				StartInfo='Time:  05/19/2021 20:57:11'
				TotalInfo='Elapsed time : 00:00:03'
				GroupOptions=0
				TaskDataOptions(Memory=8)
				ProfileItem('  Mesh (phi surface)', 1, 0, 0, 0, 59660, 'I(1, 0, \'772 triangles\')', true, true)
			$end 'ProfileGroup'
			$begin 'ProfileGroup'
				MajorVer=2021
				MinorVer=1
				Name='Adaptive Meshing'
				StartInfo='Time:  05/19/2021 20:57:17'
				TotalInfo='Elapsed time : 00:09:19'
				GroupOptions=124
				TaskDataOptions()
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 1'
					StartInfo='Time:  05/19/2021 20:57:17'
					TotalInfo='Elapsed time : 00:00:09'
					GroupOptions=740293168
					TaskDataOptions()
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c022 Using 16 core(s); 196496116 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 1, 0, 7, 0, 285616, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 1, 0, 7, 0, 285616, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 2'
					StartInfo='Time:  05/19/2021 20:57:26'
					TotalInfo='Elapsed time : 00:00:13'
					GroupOptions=124
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 61872, 'I(1, 0, \'2142 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c022 Using 16 core(s); 196496116 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 2, 0, 8, 0, 450732, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 3, 0, 23, 0, 450732, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 3'
					StartInfo='Time:  05/19/2021 20:57:39'
					TotalInfo='Elapsed time : 00:00:13'
					GroupOptions=740293168
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 0, 0, 0, 0, 61872, 'I(1, 0, \'4630 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c022 Using 16 core(s); 196496116 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 2, 0, 13, 0, 627320, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 7, 0, 88, 0, 633960, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 4'
					StartInfo='Time:  05/19/2021 20:57:53'
					TotalInfo='Elapsed time : 00:00:23'
					GroupOptions=124
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 1, 0, 0, 0, 61944, 'I(1, 0, \'9600 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c022 Using 16 core(s); 196496116 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 2, 0, 20, 0, 665204, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 12, 0, 176, 0, 786788, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 5'
					StartInfo='Time:  05/19/2021 20:58:17'
					TotalInfo='Elapsed time : 00:00:36'
					GroupOptions=740293168
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 1, 0, 0, 0, 70132, 'I(1, 0, \'19852 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c022 Using 16 core(s); 196496116 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 2, 0, 34, 0, 921924, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 28, 0, 415, 0, 1263148, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 6'
					StartInfo='Time:  05/19/2021 20:58:54'
					TotalInfo='Elapsed time : 00:01:02'
					GroupOptions=124
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 1, 0, 1, 0, 109832, 'I(1, 0, \'39680 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c022 Using 16 core(s); 196496116 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 5, 0, 58, 0, 1003500, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 52, 0, 784, 0, 1739236, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 7'
					StartInfo='Time:  05/19/2021 20:59:57'
					TotalInfo='Elapsed time : 00:01:39'
					GroupOptions=124
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 3, 0, 2, 0, 183316, 'I(1, 0, \'76762 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c022 Using 16 core(s); 196496116 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 8, 0, 88, 0, 1352588, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 80, 0, 1225, 0, 2738584, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				$begin 'ProfileGroup'
					MajorVer=2021
					MinorVer=1
					Name='Pass 8'
					StartInfo='Time:  05/19/2021 21:01:36'
					TotalInfo='Elapsed time : 00:04:59'
					GroupOptions=740293168
					TaskDataOptions()
					ProfileItem('  Mesh (surface, adaptive)', 6, 0, 4, 0, 315976, 'I(1, 0, \'143178 triangles\')', true, true)
					ProfileItem('  Machine Configuration', 0, 0, 0, 0, 0, 'I(1, 0, \'c022 Using 16 core(s); 196496116 K aval. mem.\')', false, true)
					ProfileItem('  Solver setup', 19, 0, 260, 0, 3035864, 'I(1, 0, \'16 core(s)\')', true, true)
					ProfileItem('  Matrix solution', 267, 0, 4113, 0, 6929256, 'I(1, 0, \'16 core(s)\')', true, true)
				$end 'ProfileGroup'
				ProfileFootnote('I(1, 0, \'Adaptive Passes converged\')', 0)
			$end 'ProfileGroup'
			ProfileFootnote('I(1, 0, \'Time:  05/19/2021 21:06:36, Status: Normal Completion\')', 0)
		$end 'ProfileGroup'
	$end '56001'
$end 'Profile'
