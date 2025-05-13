import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

/**
 * Класс для генерации псевдослучайной бинарной последовательности
 * и записи её в файл
 */
public class generator { 
    
    /**
     * Метод класса создаёт объект для генерации случайной последовательности, которая в итоге
     * преобразуется в строковый формат. Полученный результат выводится на экран и записывается в файл
     * 
     * @param args аргументы командной строки (не используются, но необходимо для работы метода класса)
     * 
     * @throws IOException вызывается в случае появления ошибки при записи файла
     */
    public static void main(String[] args) {
        Random random = new Random();
        
        StringBuilder binarySequence = new StringBuilder(128);

        for (int i = 0; i < 128; i++) {
            binarySequence.append(random.nextInt(2)); 
        }

        String sequence = binarySequence.toString();
        System.out.println("Псевдослучайная бинарная последовательность: " + sequence);

        try (FileWriter fileWriter = new FileWriter("sequence_java.txt")) {
            fileWriter.write(sequence);
            System.out.println("Последовательность успешно записана в файл sequence_java.txt");
        } catch (IOException e) {
            System.err.println("Ошибка при записи в файл: " + e.getMessage());
        }
    }
}
