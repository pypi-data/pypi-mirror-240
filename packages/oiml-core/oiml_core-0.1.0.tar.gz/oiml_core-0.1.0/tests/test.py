import unittest
import oiml_core

class Empty(unittest.TestCase):
    def test_1(self):
        src = ""
        res = oiml_core.parse(src)
        self.assertLessEqual(len(res), 0, 'empty string should output empty list of block')
    def test_2(self):
        src = '      '
        res = oiml_core.parse(src)
        self.assertLessEqual(len(res), 0, 'empty string should output empty list of block')
    def test_3(self):
        src = '// comment comment'
        res = oiml_core.parse(src)
        self.assertLessEqual(len(res), 0, 'empty string should output empty list of block')
    def test_4(self):
        src = '   \n    \t \n  // comment comment\n\n'
        res = oiml_core.parse(src)
        self.assertLessEqual(len(res), 0, 'emtpy string should output empty list of block')


class SimpleCmd(unittest.TestCase):
    def test_1(self):
        src = 'a'
        res = oiml_core.parse(src)
        self.assertEqual(len(res), 1, 'should output 1 block')
        self.assertEqual(res[0].B, None, 'should have no B part')
        self.assertEqual(res[0].C, None, 'should have no C part')
        self.assertTrue(bool(res[0].A), 'should have an A part')
        self.assertEqual(len(res[0].A), 1, 'should have an A part of length 1.')
        self.assertEqual(type(res[0].A[0]), str, 'first element of A part should be string.')
        self.assertEqual(res[0].A[0], 'a', 'first element of A part should be "a".')

    def test_2(self):
        src = 'a b c #true #false 0x3 4.5'
        res = oiml_core.parse(src)
        self.assertEqual(len(res), 1, 'should output 1 block')
        self.assertEqual(res[0].B, None, 'should have no B part')
        self.assertEqual(res[0].C, None, 'should have no C part')
        self.assertTrue(bool(res[0].A), 'should have an A part')
        self.assertEqual(len(res[0].A), 7, 'should have an A part of length 7')
        self.assertIs(type(res[0].A[0]), str, 'first element of A part should be string')
        self.assertIs(type(res[0].A[1]), str, 'first element of A part should be string')
        self.assertIs(type(res[0].A[2]), str, 'first element of A part should be string')
        self.assertIs(type(res[0].A[3]), bool, 'first element of A part should be bool')
        self.assertIs(type(res[0].A[4]), bool, 'first element of A part should be bool')
        self.assertIs(type(res[0].A[5]), int, 'first element of A part should be int')
        self.assertIs(type(res[0].A[6]), float, 'first element of A part should be float')
        self.assertEqual(res[0].A[0], 'a', 'first element of A part should be "a".')
        self.assertEqual(res[0].A[1], 'b', 'second element of A part should be "b".')
        self.assertEqual(res[0].A[2], 'c', 'third element of A part should be "c".')
        self.assertEqual(res[0].A[3], True, 'fourth element of A part should be True.')
        self.assertEqual(res[0].A[4], False, 'fifth element of A part should be False.')
        self.assertEqual(res[0].A[5], 0x3, 'sixth element of A part should be 0x3.')
        self.assertEqual(res[0].A[6], 4.5, 'seventh element of A part should be 4.5.')

    def test_3(self):
        src = '0x3 0o4 0b1001 3 4.5 -0.67 8.69e10 4.56E2 -9.10e-3'
        res = oiml_core.parse(src)
        self.assertEqual(len(res), 1, 'should output 1 block')
        self.assertEqual(res[0].B, None, 'should have no B part')
        self.assertEqual(res[0].C, None, 'should have no C part')
        self.assertTrue(bool(res[0].A), 'should have an A part')
        self.assertEqual(len(res[0].A), 9, 'should have an A part of length 9')
        self.assertIs(type(res[0].A[0]), int, 'first element of A part should be int')
        self.assertIs(type(res[0].A[1]), int, 'second element of A part should be int')
        self.assertIs(type(res[0].A[2]), int, 'third element of A part should be int')
        self.assertIs(type(res[0].A[3]), int, 'fourth element of A part should be int')
        self.assertIs(type(res[0].A[4]), float, 'fifth element of A part should be float')
        self.assertIs(type(res[0].A[5]), float, 'sixth element of A part should be float')
        self.assertIs(type(res[0].A[6]), float, 'seventh element of A part should be float')
        self.assertIs(type(res[0].A[7]), float, 'eighth element of A part should be float')
        self.assertIs(type(res[0].A[8]), float, 'ninth element of A part should be float')
        self.assertEqual(res[0].A[0], 0x3, "first element of A part incorrect.")
        self.assertEqual(res[0].A[1], 4, "second element of A part incorrect.")
        self.assertEqual(res[0].A[2], 9, "third element of A part incorrect.")
        self.assertEqual(res[0].A[3], 3, "fourth element of A part incorrect.")
        self.assertEqual(res[0].A[4], 4.5, "fifth element of A part incorrect.")
        self.assertEqual(res[0].A[5], -0.67, "6th element of A part incorrect.")
        self.assertEqual(res[0].A[6], 8.69e10, "7th element of A part incorrect.")
        self.assertEqual(res[0].A[7], 4.56E2, "8th element of A part incorrect.")
        self.assertEqual(res[0].A[8], -9.10e-3, "9th element of A part incorrect.")

    def test_4(self):
        src = "0xvz 0b9 0oaf"
        res = oiml_core.parse(src)
        self.assertEqual(len(res), 1, 'should output 1 block')
        self.assertEqual(res[0].B, None, 'should have no B part')
        self.assertEqual(res[0].C, None, 'should have no C part')
        self.assertTrue(bool(res[0].A), 'should have an A part')
        self.assertEqual(len(res[0].A), 3, 'should have an A part of length 3')
        self.assertIs(type(res[0].A[0]), str, 'first element of A part should be string')
        self.assertIs(type(res[0].A[1]), str, 'second element of A part should be string')
        self.assertIs(type(res[0].A[2]), str, 'third element of A part should be string')
        self.assertEqual(res[0].A[0], "0xvz", "first element of A part incorrect.")
        self.assertEqual(res[0].A[1], "0b9", "second element of A part incorrect.")
        self.assertEqual(res[0].A[2], "0oaf", "third element of A part incorrect.")

    def test_5(self):
        src = "a \"b\" \\c blah\\ \\:d"
        res = oiml_core.parse(src)
        self.assertEqual(len(res), 1, 'should output 1 block')
        self.assertEqual(res[0].B, None, 'should have no B part')
        self.assertEqual(res[0].C, None, 'should have no C part')
        self.assertTrue(bool(res[0].A), 'should have an A part')
        self.assertEqual(len(res[0].A), 4, 'should have an A part of length 4')
        self.assertIs(type(res[0].A[0]), str, "first element of A part should be string.")
        self.assertIs(type(res[0].A[1]), str, "second element of A part should be string.")
        self.assertIs(type(res[0].A[2]), str, "third element of A part should be string.")
        self.assertIs(type(res[0].A[3]), str, "fourth element of A part should be string.")
        self.assertEqual(res[0].A[0], "a", "first element of A part incorrect.")
        self.assertEqual(res[0].A[1], "b", "second element of A part incorrect.")
        self.assertEqual(res[0].A[2], "c", "third element of A part incorrect.")
        self.assertEqual(res[0].A[3], "blah :d", "third element of A part incorrect.")

    def test_6(self):
        src = "a b c:"
        res = oiml_core.parse(src)
        self.assertEqual(len(res), 1, 'should output 1 block')
        self.assertIsNot(res[0].B, None, 'should have a B part')
        self.assertEqual(res[0].C, None, 'should have no C part')
        self.assertTrue(bool(res[0].A), 'should have an A part')
        self.assertEqual(len(res[0].A), 3, 'should have an A part of length 3')
        self.assertEqual(res[0].B, '', 'should have a B part of ""')

    def test_7(self):
        src = "a b c: blahblah\\ dsfsf"
        res = oiml_core.parse(src)
        self.assertEqual(len(res), 1, 'should output 1 block')
        self.assertIsNot(res[0].B, None, 'should have a B part')
        self.assertEqual(res[0].C, None, 'should have no C part')
        self.assertTrue(bool(res[0].A), 'should have an A part')
        self.assertEqual(len(res[0].A), 3, 'should have an A part of length 3')
        self.assertEqual(res[0].B, 'blahblah\\ dsfsf', 'should have a B part of "blahblah\\\\ dsfsf"')

    def test_8(self):
        src = "a b=3 c: blahblah\\ dsfsf"
        res = oiml_core.parse(src)
        self.assertEqual(len(res), 1, 'should output 1 block')
        self.assertIsNot(res[0].B, None, 'should have a B part')
        self.assertEqual(res[0].C, None, 'should have no C part')
        self.assertTrue(bool(res[0].A), 'should have an A part')
        self.assertEqual(len(res[0].A), 3, 'should have an A part of length 3')
        self.assertEqual(res[0].B, 'blahblah\\ dsfsf', 'should have a B part of "blahblah\\\\ dsfsf"')
        self.assertEqual(type(res[0].A[1]), tuple, 'the second element of A should be a kvpair.')
        self.assertEqual(res[0].A[1][0], 'b', 'the key of the second element of A should be "b"')
        self.assertEqual(res[0].A[1][1], 3, 'the value of the second element of A should be 3')
        
    def test_9(self):
        src = "a b c\nd e f"
        res = oiml_core.parse(src)
        self.assertEqual(len(res), 2, 'should output 2 block')
        self.assertIs(res[0].B, None, 'first block should not have any B part')
        self.assertIs(res[1].B, None, 'second block should not have any B part')
    
class Block(unittest.TestCase):
    def test_1(self):
        src = '''
a b c: blahblah
    blah1 blah2 blah3
'''
        res = oiml_core.parse(src)
        self.assertEqual(len(res), 1, 'should output 1 block')
        self.assertTrue(bool(res[0].A), 'should have an A part')
        self.assertTrue(bool(res[0].B), 'should have an B part')
        self.assertTrue(bool(res[0].C), 'should have an C part')
        self.assertEqual(len(res[0].C), 1, 'C part should be of length 1')


    def test_2(self):
        src = '''
a b c: 
    blah1 blah2 blah3:
       blah1 blah2 blah3
    blah1 blah2 blah3
'''
        res = oiml_core.parse(src)
        self.assertEqual(len(res), 1, "should output 1 block")
        self.assertTrue(bool(res[0].A), 'should have an A part')
        self.assertEqual(res[0].B, '', 'should have a B part which is empty')
        self.assertTrue(bool(res[0].C), 'should have a C part')
        self.assertEqual(len(res[0].C), 2, 'should have a C part of length 2')
        self.assertFalse(bool(res[0].C[1].B), 'B part of the second child block should be undefined.')


    def test_3(self):
        src = '''
a b c: 
    blah1 blah2 blah3:
       blah1 blah2 blah3
      blah1 blah2 blah3
  blahxblahx z
'''
        try:
            res = oiml_core.parse(src)
            self.assertTrue(False, 'should raise exception for invalid indent.')
        except:
            self.assertTrue(True, '')

        
if __name__ == '__main__':
    unittest.main()
    
