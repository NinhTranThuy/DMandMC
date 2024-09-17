import java.io.*;
import java.util.*;
import java.nio.file.*;
import java.util.stream.Collectors;
public class StandardScaling {
    public static void main(String[] args) {
        String inputFile = "data3.csv";
        String outputFile = "data4.csv";

        try {
            //Doc data3.csv luu vao List<String> data
            List<String[]> data = Files.lines(Paths.get(inputFile))
                                .map(line ->line.split(","))
                                .collect(Collectors.toList());
            //In ra man hinh du lieu data
            for (String[] record:data){
                for (String cell : record){
                    System.out.print(cell + " ");
                }
                System.out.println();
            }

            //Dem so cot (hang tieu de)
            int numColumns = data.get(0).length;

            //Tao mang luu min max
            float[] minValues = new float[numColumns];
            float[] maxValues = new float[numColumns];
            Arrays.fill(minValues,Float.MAX_VALUE);
            Arrays.fill(maxValues,Float.MIN_VALUE);

            // Tim Min Max
            for (int i=1; i<data.size(); i++){
                for (int j=0; j<numColumns; j++){
                    try {
                        float value = Float.parseFloat(data.get(i)[j]);
                        minValues[j] = Math.min(minValues[j], value);
                        maxValues[j] = Math.max(maxValues[j], value);
                    } catch (NumberFormatException e) {
                        // TODO: handle exception
                    }
                }
            }

            
            // Chuan hoa Simple Scaling
            for (int i = 1 ; i < data.size(); i++){
                for (int j = 0; j < numColumns; j++){
                    try {
                        float value = Float.parseFloat(data.get(i)[j]);
                        float simpleScaling = value / maxValues[j];
                        data.get(i)[j] = String.format("%.2f", simpleScaling); 
                    } catch (NumberFormatException e) {
                    }
                }
            }
            System.out.println("Simple Scaling completed!");


            
            // // Chuan hoa Min-Max Scaling
            for (int i=1; i < data.size(); i++){
                for (int j=0; j<numColumns; j++){
                    try {
                        float value = Float.parseFloat(data.get(i)[j]);
                        float MinMaxScalingValue = (value - minValues[j]) / (maxValues[j] - minValues[j]);
                        data.get(i)[j] = String.format("%.2f", MinMaxScalingValue);
                    } catch (NumberFormatException e) {
                    }
                }
            }
            System.out.println("Min-Max Scaling completed!");



            // Chuan hoa Z-score
            //Mau phuong sai (n-1)

            //Tinh Trung binh
            float[] AverageValue = new float[numColumns];
            Arrays.fill(AverageValue,0);
          
            for (int i=1; i<data.size(); i++){
                for (int j=0; j < numColumns; j++){
                    try {
                        float value = Float.parseFloat(data.get(i)[j]);
                        AverageValue[j] += value;
                    } catch (NumberFormatException e) {
                    }
                }
            }

            for (int j=0; j<numColumns; j++){
                AverageValue[j] /= (data.size()-1);
            }

            //Tinh Phuong sai
            float[] DMValue = new float[numColumns];
            Arrays.fill(DMValue,0);
            for (int i=1; i<data.size(); i++){
                for (int j=0; j < numColumns; j++){
                    try {
                        float value = Float.parseFloat(data.get(i)[j]);
                        DMValue[j] += Math.pow(value - AverageValue[j], 2);
                    } catch (NumberFormatException e) {
                    }
                }
            }

            for (int j=0; j<numColumns; j++){
                DMValue[j] = (float)Math.sqrt(DMValue[j]/((data.size()-1)-1));
            }

            // Tinh Z-score
            for (int i=1; i<data.size(); i++){
                for (int j=0; j < numColumns; j++){
                    try {
                        float value = Float.parseFloat(data.get(i)[j]);
                        float ZScore = (value - AverageValue[j])/DMValue[j];
                        data.get(i)[j] = String.format("%.2f", ZScore);
                        } catch (NumberFormatException e) {
                    }
                }
            }

            System.out.println("Z-score Scaling completed!");

            


            //In ra man hinh ket qua
            for (String[] record:data){
                for (String cell : record){
                    System.out.print(cell + " ");
                }
                System.out.println();
            }

            // Xuat file csv data4.csv
            try (PrintWriter printWriter = new PrintWriter(new File(outputFile))){
                for (String[] row : data){
                    printWriter.println(String.join(",", row));
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}
