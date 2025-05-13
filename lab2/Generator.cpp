#include <iostream>
#include <random>
#include <fstream>
#include <bitset>
/*
  Генерирует бинарной псевдослучайную последовательность и сохраняет её в файл
  
  В случае неуспешного сохранения в файл вызовет исключение
  
  Параметры:
  filename - путь для сохранения файла
*/
void generateAndSaveSequence(const std::string& filename) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::ofstream outFile(filename);

    if (!outFile) {
        std::cerr << "Ошибка открытия файла" << std::endl;
        return;
    }

    std::bitset<128> bits;
    for (int j = 0; j < 128; j++) {
        bits[j] = gen() % 2; 
    }

    outFile << bits.to_string() << std::endl; 
    outFile.close();
}
/*
  Главная функция программы

  Вызывает generateAndSaveSequence с названием сохраняемого файла "sequence_cpp.txt"
*/
int main() {
    const std::string filename = "sequence_cpp.txt"; 

    generateAndSaveSequence(filename);

    return 0;
}
