
from intelliw_onnx.convert import ONNXConvert, ConvertArgs

"""
 python main.py convert --model_path ./model_path/ --model_type paddle --output "./output.onnx" --input_shape '[1,3,10,10]' 
 --model_def_file './test_onnx_demo.py' 
 --model_class_name 'MyModel'  
 --params_file ./params.py
"""

if __name__ == '__main__':
    args = ConvertArgs(model_path='/Users/hexer/Downloads/roformer-chinese-sim-char-ft-base/',
                       model_type='paddle',
                       output='./test_pd_model.onnx',

                       )
    converter = ONNXConvert(args)
    converter.convert()
