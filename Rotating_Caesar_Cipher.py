class Rotating_CC:
    ALPHA = ('A','B','C','D','E','F','G','H','I','J','K','L','M',
             'N','O','P','Q','R','S','T','U','V','W','X','Y','Z')

    alpha = ('a','b','c','d','e','f','g','h','i','j','k','l','m',
             'n','o','p','q','r','s','t','u','v','w','x','y','z')

    def RCC_encrypt(self, msg, shift):
        return self.RCC(msg, shift)

    def RCC_decrypt(self, msg, shift):
        # TODO - delete 'pass' and replace with the correct code to decrypt.
        # note - the shift parameter is the encryption integer.
        pass

    def RCC(self, msg, shift):
        new_msg = ""
        new_shift = shift

        for ch in msg:
            if ch in self.ALPHA:
                i = self.ALPHA.index(ch)
                ch = self.ALPHA[i + new_shift]

            elif ch in self.alpha:
                i = self.alpha.index(ch)
                ch = self.alpha[i + new_shift]

            new_shift += shift
            new_msg += ch

        return new_msg