from torch.utils.data import Dataset

class RemoveLabel(Dataset):
    """ Remove Label from a Dataset """
    def __init__(self, dataset):
        self.dataset = dataset

    def __getitem__(self, index):
        # Delete label
        image, _ = self.dataset[index]
        return image
    
    def __len__(self):
        # Method required for using suffle = True in DataLoader
        return len(self.dataset)