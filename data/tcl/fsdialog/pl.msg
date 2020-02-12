
namespace eval ::ttk::dialog::file {   
    ::msgcat::mcset pl Open			{Otwórz}
    ::msgcat::mcset pl {Save As}		{Zapisz pod nazwą}
    ::msgcat::mcset pl Cancel			Zaniechaj
    ::msgcat::mcset pl Clear			Wyczyść
    ::msgcat::mcset pl Location			Lokalizacja
    ::msgcat::mcset pl Filter			{Rodzaj pliku}
    ::msgcat::mcset pl Name			Nazwa
    ::msgcat::mcset pl Size			Rozmiar
    ::msgcat::mcset pl Date			{Data modyfikacji}
    ::msgcat::mcset pl Permissions		{Prawa dostępu}
    ::msgcat::mcset pl Owner			Właściciel
    ::msgcat::mcset pl Group			Grupa
    ::msgcat::mcset pl Folder			Katalog
    ::msgcat::mcset pl Sorting			Sortowanie
    ::msgcat::mcset pl Reverse			Odwrotnie

    ::msgcat::mcset pl {Short View}		{Widok listy}
    ::msgcat::mcset pl {Detailed View}		{Widok szczegółowy}
    ::msgcat::mcset pl {Show Hidden Files}	{Pokaż ukryte pliki}
    ::msgcat::mcset pl {Separate Folders}	{Katalogi osobno}
    ::msgcat::mcset pl {By Name}		{Według nazwy}
    ::msgcat::mcset pl {By Date}		{Według daty}
    ::msgcat::mcset pl {By Size}		{Według rozmiaru}
    ::msgcat::mcset pl {Folders First}		{Najpierw katalogi}
    ::msgcat::mcset pl {New Folder}		{Nowy katalog}
    ::msgcat::mcset pl {Create new folder in}	{Utwórz nowy katalog w}

    ::msgcat::mcset pl {File "%s" already exists. Do you want to overwrite it?}		"Istnieje już plik o nazwie\n\"%s\"\nCzy przekasować ten plik?"
    ::msgcat::mcset pl {File "%s" does not exist.}					"Nie stwierdzono obecności pliku o nazwie\n\"%s\""
    ::msgcat::mcset pl {Cannot change to the directory "%s". Permission denied.}	"Nie udało się przejść do katalogu\n\"%s\"\n(odmowa dostępu)"
}

