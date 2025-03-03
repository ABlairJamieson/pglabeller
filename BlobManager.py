from Blob import Blob

class BlobManager:
    def __init__(self):
        self.blobs = []
        self.selected_blobs = set()  # Store selected blobs
        self.total_blobs = 0
        self.thickness = 5

    def add_blob(self, x, y, r):
        """Add a blob to the list."""
        new_blob = Blob(self.total_blobs, x, y, r)
        self.blobs.append(new_blob)
        self.total_blobs += 1

    def get_blobs(self):
        """Return the list of all blobs."""
        return self.blobs

    def get_selected_blobs(self):
        """Return the set of selected blobs."""
        return self.selected_blobs

    def select_blob(self, blob):
        """Add a blob to the selection set."""
        if blob in self.blobs:
            self.selected_blobs.add(blob)

    def deselect_blob(self, blob):
        """Remove a blob from the selection set."""
        self.selected_blobs.discard(blob)

    def toggle_selection(self, blob):
        """Toggle selection of a blob."""
        if blob in self.selected_blobs:
            self.selected_blobs.discard(blob)  # Deselect if already selected
        else:
            self.select_blob(blob) # Select if not already selected

    def is_selected(self, blob):
        if blob in self.selected_blobs:
            return True
        return False
                
    def clear_selection(self):
        """Clear all selected blobs."""
        self.selected_blobs.clear()

    def set_thickness(self, thickness):
        self.thickness = thickness

    def get_thickness(self):
        return self.thickness

    def reset(self):
        """Reset the BlobManager."""
        self.blobs.clear()
        self.selected_blobs.clear()
        self.total_blobs = 0

    def delete_selected_blobs(self):
        """Delete all selected blobs from the original list without iterator invalidation."""
        for blob in list(self.selected_blobs):  # Iterate over a copy to avoid modification issues
            if blob in self.blobs:
                self.blobs.remove(blob)
        self.selected_blobs.clear()

 
        


'''
from Blob import Blob

class BlobManager:
    def __init__(self):
        self.blobs = []
        self.selected_blob = None
        self.total_blobs = 0
        self.thickness = 5
        
    def add_blob(self, x, y, r):
        """Add a blob to the array."""
        self.blobs.append(Blob(self.total_blobs, x, y, r))
        self.total_blobs += 1
        
    def get_blobs(self):
        """Return the list of all blobs."""
        return self.blobs

    def get_selected_blob(self):
        """Return the list of all blobs."""
        return self.selected_blob

    def set_selected_blob(self, blob):
        """Return the list of all blobs."""
        self.selected_blob = blob

    def set_thickness(self, thickness):
        self.thickness = thickness

    def get_thickness(self):
        return self.thickness

    def reset(self):
        self.blobs = []
        self.selected_blob = None
        self.total_blobs = 0


    def delete_selected_blob(self):
        """Delete the currently selected blob from the blobs list."""
        if self.selected_blob is not None:
            try:
                self.blobs.remove(self.selected_blob)
                self.selected_blob = None
            except ValueError:
                print("Selected blob not found in the blobs list.")
            self.selected_blob = None
        else:
            print("No blob is currently selected.")
'''
