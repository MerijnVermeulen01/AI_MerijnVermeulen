package com.merijn.autohuur;

public class Auto {

    private String type;
    private double prijsPerDag;
    private boolean gehuurdeAuto;

    public Auto(String type, double prijsPerDag){
        this.type = type;
        this.prijsPerDag = prijsPerDag;
    }

    public void setPrijsPerDag(double prijsPerDag){
        this.prijsPerDag = prijsPerDag;
    }

    public double getPrijsPerDag(){
        return prijsPerDag;
    }

    @Override
    public String toString(){
        return type + ' ' + prijsPerDag;
    }


}
