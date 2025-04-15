#include <iostream>
#include <random>
#include <fstream>
#include <bitset>

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

int main() {
    const std::string filename = "sequence_cpp.txt"; 

    generateAndSaveSequence(filename);

    return 0;
}