// Copyright 1998-2017 Epic Games, Inc. All Rights Reserved.

#include "RacingSimGameMode.h"
#include "RacingSimPawn.h"
#include "RacingSimHud.h"

ARacingSimGameMode::ARacingSimGameMode()
{
	DefaultPawnClass = ARacingSimPawn::StaticClass();
	HUDClass = ARacingSimHud::StaticClass();
}
