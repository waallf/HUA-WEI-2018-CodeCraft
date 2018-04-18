# coding=utf-8
import sys
import os
import predictor

# def read_all_train_file():

def main(k,threshold):

    # if len(sys.argv) != 4:
    #     print 'parameter is incorrect!'
    #     print 'Usage: python esc.py ecsDataPath inputFilePath resultFilePath'
    #     exit(1)
    # Read the input files
    # ecs_infor_array = read_lines(ecsDataPath)
    # input_file_array = read_lines(inputFilePath)
    # implementation the function predictVm
    # write the result to output file
    # if len(predic_result) != 0:
    #     write_result(predic_result, resultFilePath)
    # else:
    #     predic_result.append("NA")
    #     write_result(predic_result, resultFilePath)
    # print 'main function end.'
    ecsDataPath = sys.argv[1]
    inputFilePath = sys.argv[2]
    resultFilePath = sys.argv[3]


    predictor.predict_vm(ecsDataPath, inputFilePath,resultFilePath,k,threshold )


# def write_result(array, outpuFilePath):
#     with open(outpuFilePath, 'w') as output_file:
#         for item in array:
#             output_file.write("%s\n" % item)
#
#
# def read_lines(file_path):
#     if os.path.exists(file_path):
#         array = []
#         with open(file_path, 'r') as lines:
#             for line in lines:
#                 array.append(line)
#         return array
#     else:
#         print 'file not exist: ' + file_path
#         return None


if __name__ == "__main__":
    '''
    预测总量
    '''
    # k = 0.5
    # threshold = 2
    '''
    预测单日量
    '''
    k = 6
    dict_k = {
        'flavor1':k,
        'flavor2':k,
        'flavor3':k,
        'flavor4':k,
        'flavor5':k,
        'flavor6':k,
        'flavor7':k,
        'flavor8':10,
        'flavor9':k,
        'flavor10':k,
        'flavor11':k,
        'flavor12':k,
        'flavor13':k,
        'flavor14':k,
        'flavor15':k
    }
    threshold = 2
    main(dict_k,threshold )
