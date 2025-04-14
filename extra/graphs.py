import re
import pandas as pd
import matplotlib.pyplot as plt

# === Config ===
log_file = 'training_output.log'  # Adjust if needed
output_csv = 'epoch_metrics.csv'

# === Regex Patterns ===
epoch_pattern = re.compile(r'train Epoch (\d+):')
loss_pattern = re.compile(r'f1: ([0-9.]+)')

# === Data Containers ===
epochs = []
train_loss, val_loss, test_loss = [], [], []

# === Parse Log File ===
with open(log_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

i = 0
while i < len(lines):
    line = lines[i]

    if "train Epoch" in line:
        match = epoch_pattern.search(line)
        if match:
            epoch = int(match.group(1))
            epochs.append(epoch)

            # === Train loss ===
            while i < len(lines) and not lines[i].startswith("loss:"):
                i += 1
            loss = loss_pattern.search(lines[i])
            train_loss.append(float(loss.group(1)) if loss else None)

            # === Validation loss ===
            while i < len(lines) and not lines[i].startswith("#### Validation"):
                i += 1
            i += 1
            loss = loss_pattern.search(lines[i])
            val_loss.append(float(loss.group(1)) if loss else None)

            # === Test loss ===
            while i < len(lines) and not lines[i].startswith("#### Test"):
                i += 1
            i += 1
            loss = loss_pattern.search(lines[i])
            test_loss.append(float(loss.group(1)) if loss else None)
    else:
        i += 1

# === Save to CSV ===
df = pd.DataFrame({
    'Epoch': epochs,
    'Train Loss': train_loss,
    'Validation Loss': val_loss,
    'Test Loss': test_loss
})

df.to_csv(output_csv, index=False)
print(f"Saved loss metrics to {output_csv}")

# === Plot Only Loss ===
plt.figure(figsize=(10, 5))
plt.plot(df['Epoch'], df['Train Loss'], label='Train Loss', color='blue')
plt.plot(df['Epoch'], df['Validation Loss'], label='Validation Loss', color='green')
plt.plot(df['Epoch'], df['Test Loss'], label='Test Loss', color='red')
plt.xlabel('Epoch')
plt.ylabel('f1')
plt.title('f1 over Epochs')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
