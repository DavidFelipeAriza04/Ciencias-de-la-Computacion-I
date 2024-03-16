/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Buzones;

import java.util.Scanner;

/**
 *
 * @author david
 */
public class MailBox {
    static final int N = 11;
    static final int M = 101;

    static int[][][] dp = new int[N][M][M];

    public static void main(String[] args) {
        for (int i = 0; i < M; i++)
            for (int j = i; j < M; j++)
                if (i == j) dp[0][i][j] = 0;
                else dp[0][i][j] = dp[0][j][i] = 1_000_000;

        for (int i = 1; i < N; i++) {
            for (int j = 1; j < M; j++) {
                for (int k = 0; k + j < M; k++) {
                    int mejor = 1_000_000;
                    for (int m = k + 1; m <= k + j; m++) {
                        int explota = dp[i - 1][k][m - 1];
                        int noExplota = dp[i][m][k + j];
                        mejor = Math.min(mejor, Math.max(explota, noExplota) + m);
                    }
                    dp[i][k][k + j] = mejor;
                }
            }
        }

        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        while (t-- > 0) {
            int k = scanner.nextInt();
            int m = scanner.nextInt();
            System.out.println(dp[k][0][m]);

        }
    }
}