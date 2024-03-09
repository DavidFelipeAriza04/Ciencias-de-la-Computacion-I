/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Candies;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

/**
 *
 * @author david
 */
public class Candies {

    public Candies() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese el tamaño de la matriz (filas columnas):");
        int filas = sc.nextInt();
        int columnas = sc.nextInt();
        int matriz[][] = new int[filas][columnas];
        System.out.println("Ingrese los valores de la matriz");
        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                matriz[i][j] = sc.nextInt();
            }
        }
        sc.close();
        System.out.println("Para la matriz:");
        MostrarMatriz(matriz);
        System.out.println("La mayor cantidad de dulces que se pueden obtener es "+ DividirMatriz(filas, matriz));
    }

    private void MostrarMatriz(int matriz[][]) {
        for (int fila[] : matriz) {
            System.out.println(Arrays.toString(fila));
        }
    }

    private int DividirMatriz(int filas, int matriz[][]) {
        ArrayList<Integer> ListaSumas = new ArrayList<Integer>();
        for (int i = 0; i < filas; i++) {
            ListaSumas.add(MayorCantidadDulces(matriz[i]));
        }
        int[] ArraySumas = new int[ListaSumas.size()];
        for (int i = 0; i < ArraySumas.length; i++) {
            ArraySumas[i] = ListaSumas.get(i);
        }
        return MayorCantidadDulces(ArraySumas);
    }

    private int MayorCantidadDulces(int ArraySumas[]) {
        ArrayList<Integer> ListaSumas = new ArrayList<Integer>();
        if (ArraySumas.length == 2) {
            int n1 = ArraySumas[0];
            int n2 = ArraySumas[1];
            if (n1 > n2) {
                return n1;
            } else {
                return n2;
            }
        }
        if (ArraySumas.length == 1) {
            return ArraySumas[0];
        }
        if (ArraySumas.length == 0) {
            return 0;
        } else {
            ListaSumas.add(ArraySumas[0]);
            ListaSumas.add(ArraySumas[1]);
            int n1 = 0;
            int n2 = 0;
            for (int i = 2; i < ArraySumas.length; i++) {
                if (i - 3 >= 0) {
                    n1 = ArraySumas[i] + ListaSumas.get(i - 3);
                }
                if (i - 2 >= 0) {
                    n2 = ArraySumas[i] + ListaSumas.get(i - 2);
                }
                if (n1 > n2) {
                    ListaSumas.add(n1);
                } else {
                    ListaSumas.add(n2);
                }
                // print(ListaSumas)
            }

        }
        if (ListaSumas.get(ListaSumas.size()- 1)>ListaSumas.get(ListaSumas.size()- 2))
            return ListaSumas.get(ListaSumas.size() - 1);
        else
            return ListaSumas.get(ListaSumas.size() - 2);
    }

    public static void main(String[] args) {
        new Candies();
    }

}
