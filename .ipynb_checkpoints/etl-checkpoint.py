
tsf1_1={1:['WORLD']}
tsf1_2={2:['APPLE']}

tsfm_1={1: ['WORLD', 'GSCHOOLERS']}
tsfm_2={2: ['CAT', 'DOG']}

tsfmk_1= {1: ['APPLE', 'ARTICHOKE'], 2: ['BOAT', 'BALLERINA']}
tsfmk_2= {1: ['PINEAPPLE', 'ANSJOVIE'], 2: ['TOMATO', 'MEATBALL']}

old = {
            1: "AEIOULNRST",
            2: "DG",
            3: "BCMP",
            4: "FHVWY",
            5: "K",
            8: "JX",
            10: "QZ",
        }

old = {
            1: "a",
            2: "b",
            3: "c",
            4: "d",
            5: "e",
            8: "f",
            10: "g",
        }

class etl:
    
    @staticmethod
    def transform(data):
        new_dict={}
        for k,v in data.items():
            print(k,v)
            for item_v in sorted(v):
                new_dict[item_v.lower()]=k
        return new_dict
            
etl.transform({
            1: "AEIOULNRST",
            2: "DG",
            3: "BCMP",
            4: "FHVWY",
            5: "K",
            8: "JX",
            10: "QZ",
        })