Vim�UnDo� TWt�IT�m�e)�D
��"�rRYj��K�}�V   $                                   \�_    _�                             ����                                                                                                                                                                                                                                                                                                                                                             \�Y     �                 5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             \�Z     �                 5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             \�[     �                 5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             \�\    �               %   #!/usr/bin/env python3       
import sys   import numpy as np   !from scipy.io.wavfile import read   import matplotlib.pyplot as plt           if (len(sys.argv) < 2):   -  print("Usage: .\\audio_format.py filename")     sys.exit(0)       filename = sys.argv[1]   fs, x = read(filename)       # mix left and right to mono   !x = (x[:, 0] / 2) +( x[:, 1] / 2)       .# rescale and offset so that bounds are [0, 1]   %x_norm = x.astype(float) / np.amax(x)       # quantize and resample   Gx_rescale_8 = np.trim_zeros((x_norm * 2**7).astype(np.int8)[::2], 'fb')       *with open(filename[:-4] + ".h", 'w') as f:     f.write('#pragma once\n\n')   B  f.write('#define kAliveWaveLen {}\n\n'.format(x_rescale_8.size))   $  f.write('#include <stdint.h>\n\n')   A  f.write('static const int8_t kAliveWave[kAliveWaveLen] = {{\n')       -  for index, value in enumerate(x_rescale_8):   %    if index == x_rescale_8.size - 1:   %      f.write('  {}\n'.format(value))   	    else:   &      f.write('  {},\n'.format(value))         f.write('};\n')5�_�                             ����                                                                                                                                                                                                                                                                                                                                                             \�^    �                import matplotlib.pyplot as plt5��