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
    
    int[][] arr;
    int res;
    public MailBox() {
        Scanner scanner = new Scanner(System.in);
        int tc = scanner.nextInt(); //TestCases
        for (int i = 1; i < tc; i++) {
            int mb = scanner.nextInt(); //MailBoxes
            int fc = scanner.nextInt(); //FireCrackers
            arr = new int[mb + 1][fc + 1];
            res = mailboxes(mb, fc);
            System.out.println(res);
        }
        scanner.close();
    }

    private int mailboxes(int mb, int fc) {
        int mejor = Integer.MAX_VALUE;
        if (mb==1){
            mejor = dp(mb,0,fc);
        }
        for (int i = 1; i < fc + 1; i++) {
            arr[mb][i] = dp(mb, 1, i);
            if (arr[mb][i] < mejor) {
                mejor = arr[mb][i];
            }
        }
        return mejor;
    }

    private int dp(int mb, int i, int j) { //Dinamic Programming
        if (j >= arr[mb].length || j == 0) {
            return 0;
        }
        if (i == j) {
            return i;
        }
        if (mb == 1) {
            return (j * (j + 1) / 2) - (i * (i + 1) / 2);
        }
        if (arr[mb][j] != 0) {
            return arr[mb][j];
        }
        arr[mb][j] = j + Math.max(dp((mb - 1), i, j - 1), dp(mb, j+1, arr[mb].length-1));
        return arr[mb][j];
    }

    public static void main(String[] args) {
        new MailBox();
    }
}
