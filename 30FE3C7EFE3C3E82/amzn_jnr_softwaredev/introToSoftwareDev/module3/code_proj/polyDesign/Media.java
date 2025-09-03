public class Media {
    String title;
    String creator;

    public Media(String title, String creator){
        this.title = title;
        this.creator = creator;
    }

    public void play(){
        System.out.println("Currently playing " + this.title + " by " + this.creator);
    }
}