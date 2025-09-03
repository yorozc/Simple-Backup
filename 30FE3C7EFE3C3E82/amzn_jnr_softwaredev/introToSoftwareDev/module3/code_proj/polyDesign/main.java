public class main{
    public static void main(String[] args){
        Book greatGatsby = new Book("The Great Gatsby", "Fitzgerald", 180);

        Movie inception = new Movie("Inception", "Christopher Nolan", 148);

        Music imagineMusic = new Music("Imagine", "John Lennon", "Rock");

        mediaLibrary library = new mediaLibrary();

        library.addMedia(greatGatsby);
        library.addMedia(inception);
        library.addMedia(imagineMusic);

        library.playMedia(greatGatsby);
        library.playMedia(inception);
        library.playMedia(imagineMusic);

    
    }
}