from tests import *
from read_write_function import read_file, write_to_file

def calculate_p(sequence: str, config)->float:

    p_1 = pobit_test(sequence, config["sqrt_2"])
    p_2 = test_on_repeat_bit(sequence)
    p_3 = test_with_blocks(sequence, config["M"], pi = np.array([config["pi_1"], 
                                                                 config["pi_2"], 
                                                                 config["pi_3"], 
                                                                 config["pi_4"]]))
    
    result = f"sequence:{sequence}\nP-значение 1: {p_1}\nP-значение 2: {p_2}\nP-значение 3: {p_3}\n\n"

    return result

def main():
    try:
        config = read_file('config.json','json')
        cfg = config["Directory"]
        config_value = config["Const"]

        sequence_cpp = read_file(cfg['sequence_cpp'], 'text') 
        print(f"cpp_generator: {sequence_cpp}")

        sequence_java = read_file(cfg['sequence_java'], 'text') 
        print(f"java_generator: {sequence_java}")

        result_cpp = calculate_p(sequence_cpp, config_value)
        result_java = calculate_p(sequence_java, config_value)
        result = result_cpp + result_java

        write_to_file(cfg['P-values'], result, 'text')
        print("P-значения успешно записаны в файл")

    except Exception as e:
        print(f"Ошибка: {e}")
        return 

if __name__ == "__main__":
    main()
