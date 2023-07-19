from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image
from reportlab.lib import colors
import random

def create_bingo_card():
    bingo_card = []
    numbers_per_column = 5
    min_numbers = [1, 16, 31, 46, 61]
    max_numbers = [15, 30, 45, 60, 75]
    columns = ["B", "I", "N", "G", "O"]

    for column in range(len(columns)):
        column_values = random.sample(range(min_numbers[column], max_numbers[column] + 1), numbers_per_column)
        bingo_card.append(column_values)

    a = Image("logo.png", 0.6*inch, 0.8*inch)
    # Insert a free space in the middle of the card
    bingo_card[2][2] = a

    return bingo_card

def generate_bingo_card_pdf():
    # Create a Bingo card
    card1 = create_bingo_card()
    card2 = create_bingo_card()
    # Transpose the card to have columns instead of rows
    transposed_card1 = list(zip(*card1))
    transposed_card2 = list(zip(*card2))

    # Create a new PDF document
    doc = SimpleDocTemplate("bingo_cards.pdf", pagesize=landscape(A4))

    # Define the table data and style
    data1 = [["B", "I", "N", "G", "O"]] + transposed_card1
    data2 = [["B", "I", "N", "G", "O"]] + transposed_card2
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),  # Grey background for the BINGO row
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),  # White text for the BINGO row
        ("BACKGROUND", (0, 1), (-1, -1), colors.white),  # White background for other cells
        ("TEXTCOLOR", (0, 1), (-1, -1), colors.black),  # Black text for other cells
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),  # Center alignment for all cells
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),  # Middle alignment for all cells
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),  # Bold font for all cells
        ("FONTSIZE", (0, 1), (-1, -1), 20),  # Font size 20 for all cells
        ("BOTTOMPADDING", (0, 1), (-1, -1), 10),  # Bottom padding for all cells
        ("FONTSIZE", (0, 0), (-1, 0), 40),  # Font size 40 for header
        ("VALIGN", (0, 0), (-1, 0), 'TOP'),  # Top alignment for header
        ("TOPPADDING", (0, 0), (-1, 0), 0.2*inch),  # Top padding for header
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black)  # Add grid lines
    ]

    # Create the table and apply the style
    table1 = Table(data1, colWidths=0.9*inch, rowHeights=1*inch)
    table2 = Table(data2, colWidths=0.9*inch, rowHeights=1*inch)
    table1.setStyle(TableStyle(style))
    table2.setStyle(TableStyle(style))

    # Divide the page into two equal parts for two Bingo cards
    story = [Table([[table1, table2]])]

    # Build the PDF document and save it
    doc.build(story)

# Generate two Bingo cards on a single A4 landscape page
generate_bingo_card_pdf()
