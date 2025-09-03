public class Book extends Media{
    int numberOfPages;

    public Book(String title, String creator, int numberOfPages){
        super(title, creator);
        this.numberOfPages = numberOfPages;
    }

    @Override
    public void play(){
        System.out.println("Reading " + title + " by " + creator + " with " + numberOfPages + " pages.");
    }

}