#================(1)=================#

# translation_dict = {
#     "1": "ONE",
#     "2": "two",
#     "3": "three",
#     "4":"four",
#    "5":"five",
#    "6":"six",
#    "7":"seven",
#    "8":"eigth",
#    "9":"nine",
#    "10":"then"
# }

# with open("input.txt", "a") as input_file:
#     input_txt = translation_dict.values()
#     for x in input_txt:
#         input_file.write(x)


# with open('input.txt', 'r') as input_file:
#     input_text = input_file.read()


# output_text = input_text
# for persian, english in translation_dict.items():
#     output_text = output_text.replace(english, persian)


# with open('output.txt', 'w') as output_file:
#     output_file.write(output_text)

#================(2)=================#

# with open("input.txt", "r") as input_file:
#     input_text = input_file.read()


# with open("output-1.txt", "a") as output_file_1:
#     output_text_1 = "\n".join(input_text)
#     output_file_1.write(output_text_1)


# words = input_text.split()
# unique_words = set(words)
# numbers = [word for word in words if word.isdigit()]

# output_text_2 = f"unique words: {unique_words}\nnumber of unique words: {len(unique_words)}\nnumbers: {numbers}\nnumber of numbers: {len(numbers)}"
# with open("output-2.txt", "a") as output_file_2:
#     output_file_2.write(output_text_2)


# with open("output-3.txt", "a") as output_file_3:
#     for x in words:
#         if x.isupper():
#             output_file_3.write(x)

#================(3)=================#

#import pickle
# import dill

# class User:
#     def __init__(self, ID, first_name, last_name, phon):
#         self.ID = ID
#         self.first_name = first_name
#         self.last_name = last_name
#         self.phon = phon 

#     def __repr__(self) -> str:
#         return f"{self.ID}: {self.first_name} {self.last_name} <{self.phon}>"
    

#     def pickle_txt(self):
#         pickled = pickle.dumps(self)
#         file = open("input-2.txt", "ab")
#         file.write(pickled)
#         file.close()


#     def unpickle_txt(file):
#         with open("input-2.txt", "rb") as file:
#             file = pickle.loads(file)

    
#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"
    

#     def sort_id(self):
#         sorted_user = sorted(self.ID, reverse=True)
#         with open("output-4.txt", "a") as output_file_1:
#             for x in sorted_user:
#                 output_file_1.write(str(x) + "\n")
    

#     def filter_phon(self):
#         filtred_users_phon = [x for x in self.phon if x.startswith("919")]
#         with open("output-5.txt", "ab") as output_file_2:
#             output_file_2.write(filtred_users_phon)


# obj = User(12, "kosar", "teymoori", "09937820884")
# obj_1 = User(10, "nima", "hassani", "09197826754")
# obj.pickle_txt()
# obj_1.pickle_txt()

#================(4)=================#
# class Matrix:
#     def __init__(self, m, n):
#         self.rows = m
#         self.cols = n
#         self.matrix = [[0 for _ in range(n)] for _ in range(m)]

#     def __str__(self):
#         return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])

#     def __eq__(self, other):
#         return self.matrix == other.matrix

#     def __add__(self, other):
#         if self.rows != other.rows or self.cols != other.cols:
#             raise ValueError("Matrices must be of the same size to add")
#         result = Matrix(self.rows, self.cols)
#         result.matrix = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)]
#         return result

#     def __sub__(self, other):
#         if self.rows != other.rows or self.cols != other.cols:
#             raise ValueError("Matrices must be of the same size to subtract")
#         result = Matrix(self.rows, self.cols)
#         result.matrix = [[self.matrix[i][j] - other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)]
#         return result

#     def transpose(self):
#         result = Matrix(self.cols, self.rows)
#         result.matrix = [[self.matrix[j][i] for j in range(self.rows)] for i in range(self.cols)]
#         return result
    
# obj = Matrix(3, 5)
# print(obj.transpose())
