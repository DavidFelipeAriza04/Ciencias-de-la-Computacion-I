/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Candies;

import java.util.Arrays;
import java.util.Scanner;

/**
 *
 * @author david
 */
public class Candies {
    public Candies(){
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese el tamaño de la matriz (n m)");
        int n = sc.nextInt();
        int m = sc.nextInt();
        int matriz[][] = new int[n][m];
        System.out.println("Ingrese los valores de la matriz");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                matriz[i][j] = sc.nextInt();
            }
        }
        sc.close();
        MostrarMatriz(matriz);
    }
    
    private void MostrarMatriz(int matriz[][]) {
        for (int fila[] : matriz) {
            System.out.println(Arrays.toString(fila));
        }
    }
    
    public int DividirMatriz(int x, int y, int matriz[][]){
        ArrayList <Integer> ListaSumas = new ArrayList <Integer>();
        for i in range(x):
        ListaSumas.append(MayorCantidadDulces(matriz[i]))
        return MayorCantidadDulces(ListaSumas)
    }
}
