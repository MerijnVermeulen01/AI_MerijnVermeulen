package com.merijn.autohuur;

public class AutoHuur {

    private int aantalDagen;
    private Auto gehuurdeAuto;
    private Klant huurder;

    public AutoHuur(){
        Klant k = new Klant("Mijnheer de Vries");
        k.setKorting(10.0);
        this.setHuurder(k);

        Auto a1 = new Auto("Peugeot 207", 50);
        this.setGehuurdeAuto(a1);
        this.setAantalDagen(4);
    }

    public void setAantalDagen(int aantalDagen){
        this.aantalDagen = aantalDagen;
    }

    public Auto getGehuurdeAuto() {
        return gehuurdeAuto;
    }

    public void setGehuurdeAuto(Auto gehuurdeAuto) {
        this.gehuurdeAuto = gehuurdeAuto;
    }

    public Klant getHuurder() {
        return huurder;
    }

    public void setHuurder(Klant huurder) {
        this.huurder = huurder;
    }

    public double totaalPrijs(){
        return (gehuurdeAuto.getPrijsPerDag() - (gehuurdeAuto.getPrijsPerDag() / huurder.getKorting())) * aantalDagen;
    }

    @Override
    public String toString(){
        return getHuurder().toString() + ' ' + getGehuurdeAuto();
    }

    public static void main(String [] args){
        AutoHuur ah1 = new AutoHuur();

        System.out.print(ah1);
    }

}
