# import sys
# sys.path.append('/home/juan/Research/Codes/EGCI_package/src')
import unittest
import EGCI
import soundfile as sf

print(EGCI)

class TestEGCI(unittest.TestCase):
    def setUp(self):
        # download a record file from this url: "https://drive.google.com/file/d/1QL5GimLjGLKBIiMzoa7VXlCR4GCpWBwc/view?usp=drivesdk"
        # load this record
        self.x, self.fs = sf.read('Adenomera andre.wav')

    def test_EGCI(self):
        C, H, J = EGCI.index(self.x, lag=1024)
        self.assertEqual(C, 0.41193817358492374)
        self.assertEqual(H, 0.6282709780847155)
        self.assertEqual(J, 0.6556695883688874)
    
    def test_boundaries(self):
        boundaries_C, boundaries_H = EGCI.boundaries(1024)
        self.assertEqual(hash(tuple(boundaries_H)), -70092339737776719)
        self.assertEqual(hash(tuple(boundaries_C)), -4924003035619134662)

if __name__ == '__main__':
    unittest.main()