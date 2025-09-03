public class Movie extends Media{
    int durationInMinutes;

    public Movie(String title, String creator, int durationInMinutes){
        super(title, creator);
        this.durationInMinutes = durationInMinutes;
    }

    @Override
    public void play(){
        System.out.println("Watching " + title + " directed by " + creator + ". Duration: " + durationInMinutes + " minutes");
    }
}