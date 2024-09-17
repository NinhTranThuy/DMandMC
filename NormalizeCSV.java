import java.io.*;
import java.util.*;
import java.nio.file.*;
import java.util.stream.Collectors;

public class NormalizeCSV {
    public static void main(String[] args) {
        String inputFile = "Data3.csv";
        String outputFile = "Data4.csv";
        try {
            // Đọc dữ liệu từ Data3.csv
            List<String[]> data = Files.lines(Paths.get(inputFile))
                                        .map(line -> line.split(","))
                                        .collect(Collectors.toList());

            // Tìm giá trị min và max của mỗi cột số
            int numColumns = data.get(0).length;
            double[] minValues = new double[numColumns];
            double[] maxValues = new double[numColumns];
            Arrays.fill(minValues, Double.MAX_VALUE);
            Arrays.fill(maxValues, Double.MIN_VALUE);

            // Xác định min và max cho các cột
            for (int i = 1; i < data.size(); i++) {
                for (int j = 0; j < numColumns; j++) {
                    try {
                        double value = Double.parseDouble(data.get(i)[j]);
                        minValues[j] = Math.min(minValues[j], value);
                        maxValues[j] = Math.max(maxValues[j], value);
                    } catch (NumberFormatException e) {
                        // Bỏ qua các cột không phải số
                    }
                }
            }

            // Chuẩn hóa giá trị
            for (int i = 1; i < data.size(); i++) {
                for (int j = 0; j < numColumns; j++) {
                    try {
                        double value = Double.parseDouble(data.get(i)[j]);
                        double normalized = (value - minValues[j]) / (maxValues[j] - minValues[j]);
                        data.get(i)[j] = String.format("%.2f", normalized);
                    } catch (NumberFormatException e) {
                        // Bỏ qua các cột không phải số
                    }
                }
            }

            // Ghi kết quả ra Data4.csv
            try (PrintWriter writer = new PrintWriter(new File(outputFile))) {
                for (String[] row : data) {
                    writer.println(String.join(",", row));
                }
            }

            System.out.println("Normalization completed and written to Data4.csv.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}



// import pandas as pd
// from sklearn.preprocessing import MinMaxScaler

// # Đọc dữ liệu từ Data3.csv
// data = pd.read_csv('Data3.csv')

// # Chỉ chuẩn hóa các cột số
// numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
// scaler = MinMaxScaler()

// # Chuẩn hóa giá trị số
// data[numeric_columns] = scaler.fit_transform(data[numeric_columns])

// # Ghi kết quả ra Data4.csv
// data.to_csv('Data4.csv', index=False)

// print("Normalization completed and written to Data4.csv.")
