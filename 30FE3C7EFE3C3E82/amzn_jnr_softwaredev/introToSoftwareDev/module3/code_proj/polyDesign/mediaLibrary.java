public class mediaLibrary {
    
    public Media addMedia(Media mediaItem){
        System.out.println("Added " + mediaItem.title + " to the library");
        return mediaItem;
    }

    public void playMedia(Media mediaItem){
        mediaItem.play();
    }
}
