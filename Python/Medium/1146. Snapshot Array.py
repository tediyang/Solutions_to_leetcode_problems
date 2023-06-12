class SnapshotArray:
    def __init__(self, length: int):
        """ 
            # Get the length of the array and store it in the snapshots.
            Note: This was done to obtain a deep copy.
            # Initialize snap count to 0
            # Make a deepcopy of the array
        """
        self.snapshots = [0] * length
        self.snapcount = 0 
        self.array = self.snapshots.copy()

    def set(self, index: int, val: int) -> None:
        # Set the val to the index in the array.
        self.array[index] = val

    def snap(self) -> int:
        """
            # Increment count after every snap
            # If snapcount is 1 then reset the snapshot (removing the initial
            array created) and append the new snapshot.
            # else append the new snapshot
        """
        self.snapcount += 1
        if self.snapcount == 1:
            self.snapshots = []
            self.snapshots.append(self.array.copy())
        else:
            self.snapshots.append(self.array.copy())
        return (self.snapcount - 1)

    def get(self, index: int, snap_id: int) -> int:
        return self.snapshots[snap_id][index]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)