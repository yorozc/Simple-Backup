public class Music extends Media{
    String genre;

    public Music(String title, String creator, String genre){
        super(title, creator);
        this.genre = genre;
    }

    @Override
    public void play(){
        System.out.println("Listening to " + title + " by " + creator + " in the " + genre + " genre.");
    }
}