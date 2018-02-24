import sys


def getVATstatus(nip):
    nip=int(nip)
    czy_VAT=True
    if nip%7==0:
        czy_VAT=False
        
    response = {
            'nip' : nip,
            'czypodatnikVAT' : czy_VAT

                    }

    return response

print getVATstatus(177)
print getVATstatus(49)


if __name__ == "__main__":
    pass