import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int t = Integer.parseInt(br.readLine());

        long[] dpTable = new long[101];
        dpTable[1] = 1;
        dpTable[2] = 1;
        dpTable[3] = 1;
        dpTable[4] = 2;
        dpTable[5] = 2;

        for (int i = 6; i <= 100; i++)
        {
            dpTable[i] = dpTable[i - 1] + dpTable[i - 5];
        }

        while (t-- > 0)
        {
            int n = Integer.parseInt(br.readLine());
            System.out.println(dpTable[n]);
        }

    }
}