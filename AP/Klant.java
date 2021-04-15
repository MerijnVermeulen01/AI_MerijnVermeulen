package com.merijn.autohuur;

public class Klant {

    private String name;
    private double kortingsPercentage;

    public Klant(String name){
        this.name = name;
    }

    public void setKorting(double kortingsPercentage){
        this.kortingsPercentage = kortingsPercentage;
    }

    public double getKorting(){
        return kortingsPercentage;
    }

    @Override
    public String toString(){
        return name + ' ' + kortingsPercentage;
    }

}
